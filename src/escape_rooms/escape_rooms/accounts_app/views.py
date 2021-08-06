from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from escape_rooms.accounts_app.models import Company, Employee
from escape_rooms.accounts_app.permissions import IsSuperUser
from escape_rooms.accounts_app.serializers import CompanySerializer, EmployeeCreateUpdateSerializer, \
    EmployeeListDetailSerializer


class CompanyListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyCreateView(CreateAPIView):
    permission_classes = (IsSuperUser,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUser,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EmployeeListView(ListAPIView):
    permission_classes = (IsSuperUser,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeListDetailSerializer


class EmployeeCreateView(CreateAPIView):
    permission_classes = (IsSuperUser,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeCreateUpdateSerializer


class EmployeeDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUser,)
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method.lower() == "get":
            return EmployeeListDetailSerializer
        else:
            return EmployeeCreateUpdateSerializer

