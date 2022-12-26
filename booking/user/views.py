from django.shortcuts import render
from django.views.generic.edit import FormMixin, CreateView
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


class CreateUserView(CreateView):
    form_class = UserRegistrationForm
    model = User
    template_name = 'user/register.html'
    # def form_valid(self, form) :
    #     form.save
