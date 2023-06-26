# import form class from django
from django import forms
from .models import RoomBooking
from django.db import models

class RoomBookingForm(forms.ModelForm):
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    class Meta:
        model = RoomBooking
        exclude = ["userName"]
    