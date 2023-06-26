
from django.urls import path
from .views import roomBookingView


urlpatterns = [
    path('bookRoom/', roomBookingView, name='roomBooking'),    
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
]
