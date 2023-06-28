from django.urls import path
from .views import SignUpView, userManagementView

urlpatterns = [
    path('', userManagementView, name="userManagement"),
    path("signup/", SignUpView.as_view(), name="signup")
]