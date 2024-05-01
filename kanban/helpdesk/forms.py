from django import forms
from helpdesk.models import Category, Priority, \
  Engineer


class TicketFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        label="Enter Ticket Name"
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Select Category",
        required=False,
    )
    priority = forms.ModelChoiceField(
        queryset=Priority.objects.all(),
        empty_label="Select Priority",
        required=False
    )
    engineer = forms.ModelChoiceField(
        queryset=Engineer.objects.all(),
        empty_label="Select Engineer",
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(TicketFilterForm, self).__init__(*args, **kwargs)
        # Add additonal fields to each field's widget
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
        
    def filter_tickets(self, tickets):
        if self.cleaned_data.get("search"):
            tickets = tickets.filter(title__icontains=search_query)
        
        if self.cleaned_data.get("category"):
            tickets = tickets.filter(category=self.cleaned_data.get("category"))
        
        if self.cleaned_data.get("priority"):
            tickets = tickets.filter(priority=self.cleaned_data.get("priority"))
            
        if self.cleaned_data.get("engineer"):
            tickets = tickets.filter(assigned_to=self.cleaned_data.get("engineer"))
            
        return tickets