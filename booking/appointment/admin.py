from django.contrib import admin
from .models import Appointments
from .forms import AppointmentForm

@admin.action(description='Approve Appointments')
def approve_appointment(modeladmin, request, queryset):
    queryset.update(is_approved=True)

@admin.action(description='Reject Appointments')
def reject_appointment(modeladmin, request, queryset):
    queryset.update(is_approved=False)

@admin.action(description='Sort by appointment time.')
def sort_by_appointment_time(modeladmin, request, queryset):
    Appointments.objects.all().order_by('-appointment_time')

@admin.action(description='Sort by not approved.')
def sort_by_not_approved(modeladmin, request, queryset):
    Appointments.objects.all().filter(is_approved=False)


@admin.register(Appointments)
class AppoinmentsAdmin(admin.ModelAdmin):
    list_display = ['email', 'service', 'is_approved', 'date', 'appointment_time']
    list_filter = ['service', 'appointment_time', 'is_approved']
    date_hierarchy = 'date'
    empty_value_display = '-empty-'
    actions = [approve_appointment, reject_appointment]
    
    def get_sortable_by(self, request):
        return super().get_sortable_by('date')