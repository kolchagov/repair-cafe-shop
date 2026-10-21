from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, CreateView

from repairs.forms import RepairTicketForm, TicketSearchForm
from repairs.models import RepairTicket


class RepairTicketDetailView(DetailView):
    queryset = RepairTicket.objects.select_related('item')
    context_object_name = 'ticket'
    slug_field = 'code'
    slug_url_kwarg = 'code'
    template_name = 'repairs/ticket-details.html'


class RepairTicketCreateView(CreateView):
    model = RepairTicket
    form_class = RepairTicketForm
    template_name = 'repairs/ticket-add.html'

    def get_success_url(self):
        return reverse('repairs:details', args=[self.object.code])

def ticket_lookup(request):
    form = TicketSearchForm(request.GET or None)
    if form.is_valid():
        code = form.cleaned_data['code']
        if RepairTicket.objects.filter(code=code).exists():
            return redirect('repairs:details', code=code)
        form.add_error('code', 'No repair ticket with that code.')
    return render(request, 'repairs/ticket-search.html', {'form': form})
