from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("home")
    template_name = "registration/signup.html"

def showUsers(request):
    data = User.objects.all()
    users = {'users': data}
    print(users)
    return render(request, "home.html", users)