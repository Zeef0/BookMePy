from django.contrib import admin
from .models import Appointments

# Register your models here.

@admin.action(description='Approve Appointments')
def approve_appointment(modeladmin, request, queryset):
    queryset.update(is_approved=True)

@admin.action(description='Reject Appointments')
def reject_appointment(modeladmin, request, queryset):
    queryset.update(is_approved=False)

@admin.register(Appointments)
class AppoinmentsAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'service', 'is_approved', 'date', 'appointment_time']
    ordering = ['-date', 'appointment_time']
    actions = [approve_appointment, reject_appointment]