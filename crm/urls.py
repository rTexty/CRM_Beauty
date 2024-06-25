from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ServiceViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]