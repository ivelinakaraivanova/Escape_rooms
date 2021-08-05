from rest_framework import serializers
from rest_framework.authtoken.admin import User

from escape_rooms.accounts_app.models import Company


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

