from django.urls import path
from .views import createRoomView, deleteRoomView, getRooms

urlpatterns = [
    path("createRoom/", createRoomView, name="createRoom"),
    path("deleteRoom/", deleteRoomView, name="deleteRoom"),
    # path("home/", getRooms, name="getRoom") # will be rooms/home
]   