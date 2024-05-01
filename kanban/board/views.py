from django.views.generic import ListView
from board import models
from django.views.generic import DetailView, FormView
from helpdesk.forms import TicketFilterForm
from board.models import Column
class DashboardView(ListView):
    model = models.KanbanBoard
    template_name = 'board/dashboard.html'


class BoardView(DetailView, FormView):
    form_class = TicketFilterForm
    model = models.KanbanBoard
    template_name = 'board/board.html'

    def get_initial(self):
        initial = super().get_initial()
        # Set initial values from request.GET
        initial['search'] = self.request.GET.get('search', '')
        initial['category'] = self.request.GET.get('category', None)
        initial['priority'] = self.request.GET.get('priority', None)
        initial['engineer'] = self.request.GET.get('engineer', None)
        return initial

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        search = self.request.GET.get('search')
        category_id = self.request.GET.get('category')
        priority_id = self.request.GET.get('priority')
        engineer_id = self.request.GET.get('engineer')

        context["filters"] = {
            "search": search,
            "category": category_id,
            "priority": priority_id,
            "engineer": engineer_id
        }

        return context


class TicketView(DetailView):
    model = models.Ticket
    template_name = 'board/ticket.html'
