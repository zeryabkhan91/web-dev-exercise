from django.urls import path
from . import views

app_name = 'board'
urlpatterns = [
     path('', views.Dashboard.as_view(), name='dashboard'),
     path('board/<int:pk>/', views.BoardView.as_view(), name='board'),
]
