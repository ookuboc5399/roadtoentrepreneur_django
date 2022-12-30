from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import VideoViewSet


# router = routers.DefaultRouter()
# router.register('tasks', TaskViewSet, basename='tasks')
router = routers.DefaultRouter()
router.register('videos', VideoViewSet)


urlpatterns = [
    path('',include(router.urls)),
]