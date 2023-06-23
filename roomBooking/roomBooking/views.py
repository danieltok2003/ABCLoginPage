from django.shortcuts import render,redirect
from rooms.models import Room
from django.contrib.auth.models import User

# MASTER VIEW SETUP
def setupHomePage(request): # calls room view, user view, bookings view to display on page
    roomData = Room.objects.all()
    userData = User.objects.all()
    context = {
        'rooms' : roomData,
        'users' : userData,
    }
    return render(request, 'home.html', context)
