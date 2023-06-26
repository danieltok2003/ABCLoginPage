from django.shortcuts import render,redirect
from .forms import RoomBookingForm
# Create your views here.

def roomBookingView(request):
    context = {}
    form = RoomBookingForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("home")
    context['form'] = form
    return render(request, "roomBooking.html", context)
    
