from django.shortcuts import render
from django.views.generic import ListView
from board import models
from django.views.generic import DetailView


class Dashboard(ListView):
    model = models.KanbanBoard
    template_name = 'board/dashboard.html'


class BoardView(DetailView):
    model = models.KanbanBoard
    template_name = 'board/board.html'
