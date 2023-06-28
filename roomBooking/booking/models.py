from django.db import models
# from rooms.models import Room 
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models import Q,F

class RoomBooking(models.Model):
    roomName = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
    userName = models.ForeignKey(User, on_delete=models.CASCADE, default="", name="userName")
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()

    def clean(self):
        if self.start > self.end:
            raise ValidationError('Start should be before end')
        return super().clean()
    def save(self):
        self.full_clean()
        super(RoomBooking,self).save()
    class Meta:
        constraints = [
            models.CheckConstraint(check=Q(start__lte=F('end')), name='start_before_end')
        ]
 
    # def __str__(self):
    #     return self.roomName

