# import form class from django
from django import forms
from .models import RoomBooking

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = "__all__"