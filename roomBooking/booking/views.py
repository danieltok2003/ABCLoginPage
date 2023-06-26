from django.shortcuts import render
from .forms import RoomBookingForm
# Create your views here.

def roomBookingView(request):
    context = {}
    form = RoomBookingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "roomBooking.html", context)
