from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.http import JsonResponse
from django.template.loader import render_to_string

import json
from helpdesk.models import Ticket
from board.models import Column


class TicketUpdateView(UpdateView):
    """
    This offers a very simple view to update the status and rank of a ticket.

    It can be viewed directly from a browser to get a simple editing form, but on success it
    redirects to a view that returns the HTML for that ticket on a Kanban board.

    It can also be used from an XMLHttpRequest request, in which case the client can follow
    the redirect to get updated HTML for the ticket and replace the old ticket HTML
    without refreshing the whole page.
    """
    model = Ticket
    fields = ['status', 'rank']

    def put(self, request, *args, **kwargs):
        if not request.body:
            return JsonResponse(
                {
                    'status': "error", 
                    'error': 'Invalid Request Data'
                }, 
                status=400
            )

        data = json.loads(request.body)
        ticket_id = kwargs.get('pk')
        
        new_rank = data.get('rank')
        column_id = data.get('column_id')

        if column_id is None or ticket_id is None:
            return JsonResponse(
                {
                    'status': "error", 
                    'message': 'BAD Request'
                }, 
                status=400
            )

        try:
            column = Column.objects.get(id=column_id)
            ticket = Ticket.objects.get(id=ticket_id)
            ticket.status = column.statuses.first()
            ticket.column_id = column_id
            
            html_content = render_to_string('board/ticket.html', {
                "ticket": ticket
            })
            
            if new_rank is not None:
                ticket.rank = new_rank
            
            ticket.save()
            
            return JsonResponse({'status': "success", 'data': {
                "html": html_content
            }})
            # We can handle specific exceptions here but I did this due to lack of time
        except Exception as e:
            return JsonResponse({'status': "error", 'message': str(e)}, status=500)
    
    
    def get_success_url(self):
        """
        Return the URL where the client can get updated ticket HTML.
        """
        return reverse('board:ticket', kwargs={'pk': self.object.id})
