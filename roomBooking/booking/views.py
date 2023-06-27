from django.shortcuts import render,redirect
from .forms import RoomBookingForm
from datetime import datetime, timedelta
from .models import RoomBooking
# Create your views here.

def roomBookingView(request):
    context = {}
    form = RoomBookingForm()
    if (request.method == "POST"):
        form = RoomBookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.userName = request.user
            obj.save()
            return redirect("home")
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
    return redirect("home")
    
