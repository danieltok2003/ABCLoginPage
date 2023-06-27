from django.shortcuts import render,redirect
from .forms import CreateRoomForm, DeleteRoomForm
from .models import Room
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse_lazy

def createRoomView(request):
    if request.POST:
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        # TODO - VALIDATE IF UNIQUE ROOM NAME INPUTTED
    return render(request, 'createRoom.html', {'form' : CreateRoomForm})

def getRooms(request):
    data = Room.objects.filter()
    context = {'rooms': data}
    
    return render(request, 'home.html', context)

def modifyRooms(request, id):
    room = Room.objects.get(id=id)
    context = {
        'room' : room
    }
    return render(request, 'modifyRoom.html', context)

def updateRoom(request,id):
    roomName = request.POST['roomName']
    capacity = request.POST['capacity']
    room = Room.objects.get(id=id)
    room.roomName = roomName
    room.capacity = capacity
    room.save()
    return redirect("home")


def deleteRoomView(request,id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, 'deleteRoom.html', context)

def deleteRoomRecord(request,id):
    room = Room.objects.get(id=id)
    room.delete()
    # TODO - get ID of all users that booked room to be deleted, alert
    return redirect("home")