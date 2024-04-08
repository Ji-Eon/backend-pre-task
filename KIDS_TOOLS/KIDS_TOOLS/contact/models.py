# models.py
from django.db import models

from KIDS_TOOLS.company.models import *

class Contact(models.Model):
    # 연락처 모델
    profile_image = models.URLField(blank=True, null=True)  # 프로필 사진 URL
    name = models.CharField(max_length=100)  # 이름
    email = models.EmailField()  # 이메일
    phone_number = models.CharField(max_length=20)  # 전화번호

   
    company = models.ForeignKey(
        CompanyInfo, on_delete=models.CASCADE, related_name='Company_info')
    
    note = models.TextField(blank=True, null=True)  # 메모
    # 추가적인 필드
    address = models.CharField(max_length=255, blank=True, null=True)  # 주소
    birthday = models.DateField(blank=True, null=True)  # 생일
    website = models.URLField(blank=True, null=True)  # 웹사이트

    # 사용자 정의 라벨 (ManyToMany 관계)
    labels = models.ManyToManyField('Label', blank=True)


    created_at = models.DateField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return self.name

class Label(models.Model):
    # 라벨 모델
    name = models.CharField(max_length=100)  # 라벨 이름

    def __str__(self):
        return self.name