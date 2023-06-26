from django.db import models
# from rooms.models import Room 
from django.contrib.auth.models import User

class RoomBooking(models.Model):
    roomName = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    userName = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    # def __str__(self):
    #     return self.roomName

