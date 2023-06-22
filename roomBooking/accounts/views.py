from django.urls import reverse_lazy
from django.views import generic
from django import forms
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"