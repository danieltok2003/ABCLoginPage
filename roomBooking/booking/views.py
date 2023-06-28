from django.shortcuts import render,redirect
from .forms import RoomBookingForm, BookingModifyForm
from datetime import datetime, timedelta
from .models import RoomBooking
# Create your views here.


def bookingManagementView(request):
    bookings = RoomBooking.objects.all()
    context = {'roomBooking' :bookings}
    return render(request, "bookingManagement.html", context)

def roomBookingView(request):
    context = {}
    form = RoomBookingForm()
    if (request.method == "POST"):
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.userName = request.user
            obj.save()
            return redirect("bookingManagement")
    context['form'] = form
    return render(request, "roomBooking.html", context)

def deleteBookingView(request,id):
    booking = RoomBooking.objects.get(id=id)
    context = {'booking' : booking}
    return render(request, 'deleteBooking.html', context)

def deleteBookingRecord(request, id):
    booking = RoomBooking.objects.get(id=id)
    booking.delete()
    # TODO - get ID of all users that booked room to be deleted, alert 
    return redirect("bookingManagement")
    
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

def modifyBookingRecord(request,id):
    booking = RoomBooking.objects.get(id=id)
    booking.date = request.POST['date']
    booking.start = request.POST['start']
    booking.end = request.POST['end']
    booking.save()

    return redirect("bookingManagement")


