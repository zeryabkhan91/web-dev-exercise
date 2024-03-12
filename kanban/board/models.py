from django.db import models
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

    def get_tickets(self):
        return Ticket.objects.filter(status__in=self.statuses.all()).order_by('rank', 'id')
