from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import permissions
from .serializers import UserCreateSerializer


class UserViewSet(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all() 
    serializer_class = UserCreateSerializer
    permission_classes = [permissions.IsAdminUser]


