from django.urls import path
from . import views

app_name = 'helpdesk'
urlpatterns = [
     path('ticket/<int:pk>/', views.TicketUpdateView.as_view(), name='update-ticket'),
]
