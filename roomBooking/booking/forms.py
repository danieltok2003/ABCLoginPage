# import form class from django
from django import forms
from django.conf import settings
from .models import RoomBooking
from django.db import models
from datetimewidget.widgets import DateWidget, TimeWidget
from django.core.exceptions import ValidationError

class RoomBookingForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        exclude = ["userName"]
        widgets = {
            'date' : DateWidget(usel10n=True),
            'start' : TimeWidget(),
            'end' : TimeWidget()
        }

class BookingModifyForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        exclude = ['userName', 'roomName']
        widgets = {
            'date' : DateWidget(usel10n=True),
            'start' : TimeWidget(),
            'end' : TimeWidget()
        }
    

    