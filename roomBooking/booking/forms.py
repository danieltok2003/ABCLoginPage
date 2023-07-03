# import form class from django
from django import forms
from django.conf import settings
from .models import RoomBooking
from django.db import models
from datetimewidget.widgets import DateWidget, TimeWidget
from django.core.exceptions import ValidationError

# roomName = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
# userName = models.ForeignKey(User, on_delete=models.CASCADE, default="", name="userName")
# date = models.DateField()
# start = models.TimeField()
# end = models.TimeField()
# bookingDeleteMsg = models.CharField(default="")

class RoomBookingForm(forms.ModelForm):
    
    class Meta:
        model = RoomBooking
        fields = ["roomName", "date", "start", "end"]
        widgets = {
            'date' : DateWidget(usel10n=True),
            'start' : TimeWidget(),
            'end' : TimeWidget()
        }

class BookingModifyForm(forms.ModelForm):
    class Meta:
        model = RoomBooking
        fields = ["date", "start", "end"]
        widgets = {
            'date' : DateWidget(usel10n=True),
            'start' : TimeWidget(),
            'end' : TimeWidget()
        }
    

    