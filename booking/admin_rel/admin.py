from django.contrib import admin
from django.contrib.admin import AdminSite

from appointment.models import Appointments
class AppointmentAdminSite(AdminSite):
    site_header = "Appointments"
    site_title = "Check Appointments"
    index_title = "Administration"

admin_site = AppointmentAdminSite(name='admin_appointment_site')
# Register your models here.
admin_site.register(Appointments)