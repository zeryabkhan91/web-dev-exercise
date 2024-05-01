from django.db import models, connection
from helpdesk.models import Ticket


class KanbanBoard(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Column(models.Model):
    board = models.ForeignKey(KanbanBoard, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    statuses = models.ManyToManyField('helpdesk.Status', blank=True)

    def __str__(self):
        return self.name

    def get_tickets(self, filters):
        tickets = Ticket.objects.filter(status__in=self.statuses.all()).order_by('-rank', 'id')

        if filters.get('search'):
            tickets = tickets.filter(title__icontains=filters.get('search'))
        
        if filters.get('category'):
            tickets = tickets.filter(category=filters.get('category'))
        
        if filters.get('priority'):
            tickets = tickets.filter(priority=filters.get('priority'))
        
        if filters.get('engineer'):
            tickets = tickets.filter(assigned_to=filters.get('engineer'))
        
        tickets = tickets.prefetch_related(
            'status',
            'priority',
            'assigned_to',
            'category'
        )
        
        return tickets