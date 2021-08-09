from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from escape_rooms.accounts_app.serializers import UserCreateSerializer, UserUpdateSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserUpdateSerializer

    def get_object(self):
        return self.request.user
