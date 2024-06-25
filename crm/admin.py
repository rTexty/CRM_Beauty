
from django.contrib import admin
from .models import Client, Service, Appointment

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('client', 'service', 'date')
    list_filter = ('date', 'service')
    search_fields = ('client__first_name', 'client__last_name', 'service__name')