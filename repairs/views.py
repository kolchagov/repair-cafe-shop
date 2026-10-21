from django.shortcuts import redirect, render
from django.views.generic import DetailView

from repairs.forms import TicketSearchForm
from repairs.models import RepairTicket


class RepairTicketDetailView(DetailView):
    queryset = RepairTicket.objects.select_related('item')
    context_object_name = 'ticket'
    slug_field = 'code'
    slug_url_kwarg = 'code'
    template_name = 'repairs/ticket-details.html'


def ticket_lookup(request):
    form = TicketSearchForm(request.GET or None)
    if form.is_valid():
        code = form.cleaned_data['code']
        if RepairTicket.objects.filter(code=code).exists():
            return redirect('repairs:details', code=code)
        form.add_error('code', 'No repair ticket with that code.')
    return render(request, 'repairs/ticket-search.html', {'form': form})
