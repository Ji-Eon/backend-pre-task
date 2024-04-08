# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name','email','birthday','website','created_at')

admin.site.register(Contact, ContactAdmin)