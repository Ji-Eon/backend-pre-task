# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CompanyInfo




class CompanyAdmin(admin.ModelAdmin):

    list_display = ('id', 'company_name','position','created_at')

admin.site.register(CompanyInfo, CompanyAdmin)