from django.urls import path
from rest_framework import routers

from .views import UserViewSet


router = routers.DefaultRouter()
router.register('register', UserViewSet)

urlpatterns = [
  
] 

urlpatterns += router.urls