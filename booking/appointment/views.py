from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Appointments
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView

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
        qs = Appointments.objects.all().filter(username=self.request.user)
        return qs

class AppointmentsListView(ListView):
    model = Appointments
    context_object_name = 'context'
    queryset = Appointments.objects.all()

class CreateAppointmentView(LoginRequiredMixin, CreateView):
    model = Appointments
    form_class = AppointmentForm
    success_url = '/user/panel'
    
    def form_valid(self, form):
        form.instance.username = self.request.user
        print(self.request.session)
        return super().form_valid(form)


class UpdateAppointmentView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Appointments
    form_class = AppointmentForm

    def test_func(self):
        obj = self.get_object()
        # Test current user should be equal to the owner of the appointment
        return self.request.user == obj.username

    def form_valid(self, form):
        form.instance.username = self.request.user
        return super().form_valid(form)


class DeleteAppointmentView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Appointments
    success_url = reverse_lazy('user_panel')
    context_object_name = 'appointment'
    def test_func(self):
        obj = self.get_object()
        # Test current user should be equal to the owner of the appointment
        return self.request.user == obj.username or self.request.user.is_staff()