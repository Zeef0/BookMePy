from django.shortcuts import render

from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from appointment.models import Appointments


class AdminPanelView(UserPassesTestMixin, LoginRequiredMixin, ListView):
    model = Appointments
    queryset = Appointments.objects.all()
    template_name = 'admin_rel/dashboard.html'
    context_object_name = 'context'

    def test_func(self):
        return self.request.user.is_staff and self.request.user.is_authenticated