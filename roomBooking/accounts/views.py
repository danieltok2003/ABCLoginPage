from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django import forms
from django.contrib.auth.models import User

# Create your views here.

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'is_staff')
    


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"