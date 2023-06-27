
from django.urls import path
from .views import roomBookingView, deleteBookingView, deleteBookingRecord


urlpatterns = [
    path('bookRoom/', roomBookingView, name='roomBooking'),  
    path('deleteBooking/<int:id>', deleteBookingView, name='deleteBooking'),
    path('deleteBooking/deleteBookingRecord/<int:id>', deleteBookingRecord, name='deleteBookingRecord')  
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
