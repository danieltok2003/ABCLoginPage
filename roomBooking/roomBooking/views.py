from django.shortcuts import render
from rooms.models import Room
from django.contrib.auth.models import User
from booking.models import RoomBooking
from django.utils.timezone import localtime,now
import datetime
from django.db.models import Q

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

    # if the booking date has passed or the booking is today but the end time has passed
    passedBookings = roomBookingData.filter(Q(date__lt=time.date()) | Q(date=time.date(), end__lt=time.time()))
    passedBookings.delete()
        
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
