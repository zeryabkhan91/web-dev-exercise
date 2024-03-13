from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
     path('<int:pk>/', views.BoardView.as_view(), name='board'),
     path('ticket/<int:pk>/', views.TicketView.as_view(), name='ticket'),
]
