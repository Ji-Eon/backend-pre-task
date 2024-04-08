# serializers.py

from rest_framework import serializers
from .models import Contact, Label

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['profile_image', 'name', 'email', 'phone_number', 'company', 'address', 'birthday', 'website', 'labels']


class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name']

class ContactSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Contact
        fields = [
            'profile_image', 'name', 'email', 'phone_number', 'company', 
            'address', 'birthday', 'website', 'labels', 'created_at', 'updated_at'
        ]