from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from escape_rooms.companies_app.models import Company
from escape_rooms.companies_app.serializers import CompanySerializer


class CompanyListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateView(CreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
