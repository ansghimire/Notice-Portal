from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS

from .serializers import (
    CategorySerializer, NoticeSerializer, AdvertisementSerializer)
from .models import Category, Notice, Advertisement

from django_filters.rest_framework import DjangoFilterBackend


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [permissions.AllowAny()]
        else :
            return super().get_permissions()


class NoticeViewSet(ModelViewSet):
    serializer_class = NoticeSerializer
    queryset = Notice.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'slug', 'cateogry__category_name']
    
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [permissions.AllowAny()]
        else :
            return super().get_permissions()

    

class AdvertisementViewSet(ModelViewSet):
    serializer_class = AdvertisementSerializer
    queryset = Advertisement.objects.all()

    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return [permissions.AllowAny()]
        else :
            return super().get_permissions()

