from django.shortcuts import render,redirect
from .forms import RoomBookingForm
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
    
