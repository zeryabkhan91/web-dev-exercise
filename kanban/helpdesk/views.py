from django.views.generic.edit import UpdateView
from django.urls import reverse
from helpdesk import models


class TicketUpdateView(UpdateView):
    """
    This offers a very simple view to update the status and rank of a ticket.

    It can be viewed directly from a browser to get a simple editing form, but on success it
    redirects to a view that returns the HTML for that ticket on a Kanban board.

    It can also be used from an XMLHttpRequest request, in which case the client can follow
    the redirect to get updated HTML for the ticket and replace the old ticket HTML
    without refreshing the whole page.
    """
    model = models.Ticket
    fields = ['status', 'rank']

    def get_success_url(self):
        """
        Return the URL where the client can get updated ticket HTML.
        """
        return reverse('board:ticket', kwargs={'pk': self.object.id})
