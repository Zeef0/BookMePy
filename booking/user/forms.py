from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        print("Created")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']