from django.urls import path
from .views import createRoomView, deleteRoomView

urlpatterns = [
    path("createRoom/", createRoomView, name="createRoom"),
    path("deleteRoom/", deleteRoomView, name="deleteRoom"),
]