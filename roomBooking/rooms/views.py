from django.shortcuts import render,redirect
from .forms import CreateRoomForm
from .models import Room
# Create your views here.

def createRoomView(request):
    if request.POST:
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        # TODO - VALIDATE IF UNIQUE ROOM NAME INPUTTED
    return render(request, 'createRoom.html', {'form' : CreateRoomForm})

def deleteRoomView(request):
    roomOptions = Room.objects
    context = {'roomOptions': roomOptions}

    return render(request, 'deleteRoom.html', context)