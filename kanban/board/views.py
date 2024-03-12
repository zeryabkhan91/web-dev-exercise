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
    #
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super().get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context["book_list"] = Book.objects.all()
    #     return context