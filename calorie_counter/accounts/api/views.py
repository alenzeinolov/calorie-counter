from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .permissions import IsAnonymous
from .serializers import UserCreateSerializer, UserUpdateSerializer
from ..models import User


class UserRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return User.objects.get(username=self.request.user)


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [IsAnonymous]


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return User.objects.get(username=self.request.user)
