from multiprocessing import context
from operator import concat
from django.shortcuts import render,get_list_or_404
from django.shortcuts import get_object_or_404

import csv
import io
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
import datetime
from django.utils.dateparse import parse_date
from rest_framework.pagination import PageNumberPagination


from KIDS_TOOLS.company.models import CompanyInfo
from KIDS_TOOLS.contact.models import Contact,Label

from .serializers import ContactSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class DataView(APIView):


    def post(self, request, *args):
        '''
        Conctact 데이터 생성하기 
        '''
        csv_file_path = '/usr/src/app/media/contact_data.csv'  # CSV 파일 경로
        try:
            # CSV 파일을 열고 데이터를 읽습니다.
            with open(csv_file_path, mode='r', encoding='utf-8', errors='ignore') as file:
                reader = csv.reader(file, delimiter=',', quotechar='"')
                next(reader)  # 첫 번째 행(헤더)을 건너뜁니다.
                
                # 각 행을 순회하며 데이터를 처리합니다.
                for row in reader:
                    # 여기에 각 행을 처리하는 로직을 구현합니다.
                    # 예시: 각 row를 출력합니다.


                    company_obj, _ = CompanyInfo.objects.get_or_create(company_name=row[8], position=row[9])
                    birthday_str = row[5]
                    birthday = parse_date(birthday_str) if birthday_str else None
                    contact = Contact(
                        profile_image=row[0],
                        name=row[1],
                        email=row[2],
                        phone_number=row[3],
                        company=company_obj,
                        address=row[5],
                        birthday=birthday,
                        website=row[6],
                    )
                    contact.save()

                    labels = row[7].split(';')
                    for label_name in labels:
                        label, _ = Label.objects.get_or_create(name=label_name)
                        contact.labels.add(label)




            return Response({'message': 'CSV file processed successfully'}, status=status.HTTP_200_OK)

        except Exception as e:
            # 로그를 남기는 것이 좋습니다. 예를 들어, print(e) 또는 logging 모듈 사용
            print(e)
            # 오류가 발생한 경우, 오류 메시지와 함께 400 상태 코드를 반환합니다.
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        


class ContactListView(APIView):
    """
    연락처 목록을 조회하는 API.
    """
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ContactSortView(APIView):

    @swagger_auto_schema(
        operation_description="연락처 목록을 조회하고 정렬합니다. 정렬은 query parameter를 통해 'name', 'email', 'phone_number' 중 하나를 선택하여 정렬할 수 있습니다.",
        manual_parameters=[
            openapi.Parameter(
                'sort',
                openapi.IN_QUERY,
                description="Sort by 'name', 'email', or 'phone_number'",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'order',
                openapi.IN_QUERY,
                description="Sort order 'asc' or 'desc'",
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                'page',
                openapi.IN_QUERY,
                description="A page number within the paginated result set.",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'page_size',
                openapi.IN_QUERY,
                description="Number of results to return per page.",
                type=openapi.TYPE_INTEGER
            ),
        ]
    )

    def get(self, request, *args, **kwargs):
      
        sort_field = request.query_params.get('sort', 'id')  
        sort_order = request.query_params.get('order', 'asc')  

        # Validate sort_field
        if sort_field not in ['name', 'email', 'phone_number']:
            return Response({'error': 'Invalid sort field'}, status=status.HTTP_400_BAD_REQUEST)

        # Apply sorting
        if sort_order == 'desc':
            sort_field = f'-{sort_field}'

        paginator = PageNumberPagination()
        paginator.page_size = request.query_params.get('page_size', 10)
        paginator.page_query_param = 'page'

        contacts = Contact.objects.order_by(sort_field)
        result_page = paginator.paginate_queryset(contacts, request)
        serializer = ContactSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class ContactDetailSearchView(APIView):

    @swagger_auto_schema(
    operation_description="특정 사용자의 연락처 목록을 조회합니다.",
    responses={200: ContactSerializer})
    def get(self, request, pk, format=None):
        contact = get_object_or_404(Contact, pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)


class ContactCreateView(APIView):


    @swagger_auto_schema(
        operation_description="특정 사용자의 연락처 목록을 생성합니다..",
        request_body=ContactSerializer,
        responses={201: ContactSerializer}
    )
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)