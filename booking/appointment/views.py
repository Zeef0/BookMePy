from django.shortcuts import render
from .models import Appointments
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import AppointmentForm


class HomeView(TemplateView):
    template_name = 'appointment/home.html'


class AppointmentDetailView(LoginRequiredMixin, DetailView):
    model = Appointments
    context_object_name = "info"
class UserPanel(LoginRequiredMixin, ListView):
    model = Appointments
    context_object_name = "context"

    def get_queryset(self):
        qs = Appointments.objects.by_user(query=self.request.user)
        return qs

class AppointmentsListView(ListView):
    model = Appointments
    context_object_name = 'context'

class CreateAppointmentView(LoginRequiredMixin, CreateView):
    model = Appointments
    form_class = AppointmentForm
    success_url = '/user/panel'
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        print(self.request.session)
        return super().form_valid(form)




class AdminPanelView:
    'View where admin or staff can approve for pending appointments'
    pass