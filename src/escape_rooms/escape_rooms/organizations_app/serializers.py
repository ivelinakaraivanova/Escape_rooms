from rest_framework import serializers

from escape_rooms.accounts_app.serializers import UserNameSerializer
from escape_rooms.organizations_app.models import Company, Employee


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
