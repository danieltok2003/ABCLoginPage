from django.urls import path
from .views import createRoomView, deleteRoomView, modifyRooms, updateRoom

urlpatterns = [
    path("createRoom/", createRoomView, name="createRoom"),
    path("deleteRoom/", deleteRoomView, name="deleteRoom"),
    path("modify/<int:id>", modifyRooms, name="modifyRoom"),
    path("modify/updateRoom/<int:id>", updateRoom, name="updateRoom")
    # path("home/", getRooms, name="getRoom") # will be rooms/home
]   