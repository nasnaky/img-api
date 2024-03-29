from django.urls import path, include
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register('imgs', views.imgsView)

urlpatterns = [
    path('', include(routers.urls))
]
