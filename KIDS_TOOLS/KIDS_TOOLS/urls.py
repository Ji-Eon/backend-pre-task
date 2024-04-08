"""KIDS_TOOLS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include, reverse_lazy
from django.views.generic.base import RedirectView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions


schema_view = get_schema_view(
    openapi.Info(
        title="KIDS Note Pre Task",
        default_version='Ver1.0',
        description="Pre Task API(예: humanscape-project API 문서)",
        contact=openapi.Contact(email="medikim3551@gmail.com"), # 부가정보
        license=openapi.License(name="JIEON"),     # 부가정보
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    ###################################################################################
    # API 문서화에 관련된 부분으로 Swagger & redoc 요청에 사용되는 URL Pattern 입니다.
    ###################################################################################
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'), 
    # ...
    path('admin/', admin.site.urls),
    path('contact/', include('KIDS_TOOLS.contact.urls', namespace="contact")),
        

]
