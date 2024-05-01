from helpdesk.forms import TicketFilterForm
from django import template

register = template.Library()

@register.simple_tag
def get_filtered_tickets(column, filters):
    filter_form = TicketFilterForm(filters)
    cleaned_data = {}
    if filter_form.is_valid():
        cleaned_data = filter_form.cleaned_data
    
    tickets = column.get_tickets(cleaned_data)
    return tickets
