from django.shortcuts import render,redirect
from .forms import CreateRoomForm, DeleteRoomForm
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
    roomOptions = Room.objects.filter()
    context = {'roomOptions': roomOptions}
    # if request.POST:
    #     form = DeleteRoomForm(request.POST)
    #     Room.objects.filter(request.POST['pk']).delete()
    #     if form.is_valid():
            
    #         return redirect("home")
    return render(request, 'deleteRoom.html', context)