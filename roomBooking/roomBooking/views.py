from django.shortcuts import render
from rooms.models import Room
from django.contrib.auth.models import User
from booking.models import RoomBooking
from django.utils.timezone import localtime,now
import datetime

# MASTER VIEW SETUP
def setupHomePage(request): # calls room view, user view, bookings view to display on page
    # roomData = Room.objects.all()
    # userData = User.objects.all()
    roomBookingData = RoomBooking.objects.all()
    numBookings = RoomBooking.objects.count()

    time = localtime(now())
    numMeetingsNow = 0
    numMeetingsNow = roomBookingData.filter(date=time.date(), start__lte=time.time(), end__gte=time.time()).count()
    numRoomsAvailable = Room.objects.all().count() - numMeetingsNow
    
    context = {
        # 'rooms' : roomData,
        # 'users' : userData,
        'roomBooking' : roomBookingData,
        'numBookings' : numBookings,
        'time' : time,
        'numMeetingsNow': numMeetingsNow,
        'numRoomsAvailable': numRoomsAvailable
    }
    return render(request, 'home.html', context)
