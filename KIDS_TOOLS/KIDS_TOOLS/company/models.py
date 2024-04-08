# models.py
from django.db import models

from KIDS_TOOLS.company.models import *




class CompanyInfo(models.Model):

    
    company_name = models.CharField(max_length=100)  # 회사
    
    position = models.CharField( max_length=100, blank=True, null=True) # 직책



    created_at = models.DateField(auto_now_add=True, verbose_name="생성일")
    updated_at = models.DateField(auto_now=True, verbose_name="수정일")

    def __str__(self):
        return self.company_name

