from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import FormMixin, CreateView
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


class CreateUserView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'user/register.html'
    success_url = '/user/login'
    # def form_valid(self, form) :
    #     form.save
