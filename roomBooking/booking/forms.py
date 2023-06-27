# import form class from django
from django import forms
from .models import RoomBooking
from django.db import models
from datetimewidget.widgets import DateWidget, TimeWidget

class RoomBookingForm(forms.ModelForm):
    
    start = models.TimeField()
    end = models.TimeField()
    class Meta:
        model = RoomBooking
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii P',
            }
        exclude = ["userName"]
        widgets = {
            'date' : DateWidget()
        }
    

    