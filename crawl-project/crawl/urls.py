from . import views
from rest_framework.routers import DefaultRouter

from django.urls import path, include

router = DefaultRouter()
router.register("", views.InsertDataViewSet, basename="data")  

urlpatterns = [
    path('', include(router.urls)),
]