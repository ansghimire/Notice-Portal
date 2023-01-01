from django.urls import path
from rest_framework import routers

from .views import CategoryViewSet, AdvertisementViewSet, NoticeViewSet


router = routers.DefaultRouter()
router.register('notice', NoticeViewSet)
router.register('advertise', AdvertisementViewSet)
router.register('category', CategoryViewSet)

urlpatterns = [
  
] 

urlpatterns += router.urls