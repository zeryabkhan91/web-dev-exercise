from django.views.generic import ListView
from board import models
from django.views.generic import DetailView


class DashboardView(ListView):
    model = models.KanbanBoard
    template_name = 'board/dashboard.html'


class BoardView(DetailView):
    model = models.KanbanBoard
    template_name = 'board/board.html'


class TicketView(DetailView):
    model = models.Ticket
    template_name = 'board/ticket.html'
