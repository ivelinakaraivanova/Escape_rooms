from django.contrib.auth.models import User
from rest_framework import serializers

from escape_rooms.accounts_app.models import Company, Employee


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeListDetailSerializer(serializers.ModelSerializer):
    user = UserNameSerializer()
    company = CompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'


class EmployeeCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
