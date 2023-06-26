from django.shortcuts import render
from rooms.models import Room
from django.contrib.auth.models import User
from booking.models import RoomBooking

# MASTER VIEW SETUP
def setupHomePage(request): # calls room view, user view, bookings view to display on page
    roomData = Room.objects.all()
    userData = User.objects.all()
    roomBookingData = RoomBooking.objects.all()
    context = {
        'rooms' : roomData,
        'users' : userData,
        'roomBooking' : roomBookingData
    }
    return render(request, 'home.html', context)
