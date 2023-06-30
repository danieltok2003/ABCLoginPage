from django.shortcuts import render,redirect
from .forms import RoomBookingForm, BookingModifyForm
from datetime import datetime, timedelta
from .models import RoomBooking
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.



def bookingManagementView(request):
    # show all bookings if admin
    if request.user.is_staff:
        bookings = RoomBooking.objects.all()
    # show only own bookings if just staff
    else:
        userName = User.objects.get(username=request.user.username)
        bookings = RoomBooking.objects.filter(userName = userName)
    context = {'roomBooking' :bookings}
    return render(request, "bookingManagement.html", context)


def findBookingOverlap(newBooking):
    bookingsOnDayInRoom = RoomBooking.objects.filter(date=newBooking.date, roomName=newBooking.roomName)
    # 1. new booking completely inside another slot
    # 2. new booking completely enveloping another slot
    # 3. new booking right on top of another slot
    # 4. new booking starts before but ends inside slot
    # 5. new booking starts inside slot but ends outside slot

    overlappingSlots = bookingsOnDayInRoom.filter(
        Q(start__lt=newBooking.start, end__gt=newBooking.end) | 
        Q(start__gt=newBooking.start, end__lt=newBooking.end) |
        Q(start=newBooking.start, end=newBooking.end) |
        Q(start__gt=newBooking.start, end__gt=newBooking.end) |
        Q(start__lt=newBooking.start, end__lt=newBooking.end)
    )
    return overlappingSlots

def roomBookingView(request):
    context = {}
    form = RoomBookingForm()
    if (request.method == "POST"):
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.userName = request.user
            overlappingBookings = findBookingOverlap(obj)
            if (overlappingBookings.exists()):
                context = {
                    'overlappingBookings' : overlappingBookings,
                    'booking' : obj
                }
                return render(request, "invalidBooking.html", context)
            else:
                obj.save()
                return redirect("bookingManagement")
    context['form'] = form
    return render(request, "roomBooking.html", context)

def modifyBookingView(request,id):
    booking = RoomBooking.objects.get(id=id)
    
    data = {
        'roomName' : booking.roomName,
        'userName' : booking.userName,
        'date' : booking.date,
        'start' : booking.start,
        'end' : booking.end,        
    }
    form = BookingModifyForm(initial=data)
    return render(request, 'modifyBooking.html', {'form' : form, 'booking': booking})

def deleteBookingView(request,id):
    booking = RoomBooking.objects.get(id=id)
    context = {'booking' : booking}
    return render(request, 'deleteBooking.html', context)

def deleteBookingRecord(request, id):
    booking = RoomBooking.objects.get(id=id)
    booking.delete()
    # TODO - get ID of all users that booked room to be deleted, alert 
    return redirect("bookingManagement")
    


def modifyBookingRecord(request,id):
    if(request.method == "POST"):
        booking = RoomBooking.objects.get(id=id)
        booking.date = request.POST['date']
        booking.start = request.POST['start']
        booking.end = request.POST['end']
        booking.save()

    return redirect("bookingManagement")


