from rest_framework import serializers

from escape_rooms.companies_app.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'
