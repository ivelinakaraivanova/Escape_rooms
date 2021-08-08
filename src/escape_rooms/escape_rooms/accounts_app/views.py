from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from escape_rooms.accounts_app.models import Company, Employee
from escape_rooms.accounts_app.permissions import IsSuperUser
from escape_rooms.accounts_app.serializers import CompanySerializer, EmployeeCreateUpdateSerializer, \
    EmployeeListDetailSerializer, UserCreateSerializer, UserUpdateSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user


class CompanyListView(ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_fields = '__all__'
    search_fields = ['name']
    ordering_fields = '__all__'


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
    filterset_fields = ['company']
    # search_fields = [] no search needed
    ordering_fields = ['user__username', 'company__name']   # TODO --> user - full name


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

