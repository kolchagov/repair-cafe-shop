from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from repairs.forms import RepairTicketForm, TicketSearchForm
from repairs.models import RepairTicket, StatusChoices
from catalog.models import Item


class RepairTicketDetailView(DetailView):
    queryset = RepairTicket.objects.select_related('item')
    context_object_name = 'ticket'
    slug_field = 'code'
    slug_url_kwarg = 'code'
    template_name = 'repairs/ticket-details.html'


class RepairTicketEditView(UpdateView):
    queryset = RepairTicket.objects.select_related('item')
    form_class = RepairTicketForm
    template_name = 'repairs/ticket-edit.html'
    slug_field = 'code'
    slug_url_kwarg = 'code'

    def get_object(self, queryset=None):
        # Without a ticket code this is a create form; with one, edit that ticket and reopen it.
        if 'code' not in self.kwargs:
            return None
        self.object = super().get_object(queryset)
        if self.object.status == StatusChoices.RECEIVED:
            self.object.status = StatusChoices.IN_PROGRESS
        return self.object

    def get_initial(self):
        initial = super().get_initial()
        if item := self.request.GET.get('item'):
            initial['item'] = item
            initial['status'] = StatusChoices.IN_PROGRESS
        return initial

    def form_valid(self, form):
        # The item page already checked, but a double submit or a second volunteer can land here twice.
        # shortcut: not atomic, two simultaneous saves can still both create.
        if 'code' not in self.kwargs:
            open_ticket = RepairTicket.objects.filter(
                item=form.cleaned_data['item'],
                status__in=(StatusChoices.RECEIVED, StatusChoices.IN_PROGRESS),
            ).order_by('-updated_at').first()
            if open_ticket:
                return redirect('repairs:details', code=open_ticket.code)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('repairs:details', args=[self.object.code])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object:
            context['item'] = self.object.item
        else:
            item_id = self.request.GET.get('item', '')
            context['item'] = Item.objects.filter(pk=item_id).first() if item_id.isdigit() else None
        return context


def ticket_lookup(request):
    form = TicketSearchForm(request.GET or None)
    if form.is_valid():
        code = form.cleaned_data['code']
        if RepairTicket.objects.filter(code=code).exists():
            # ?view=true shows the Back button in details
            return redirect(reverse('repairs:details', args=[code]) + '?view=true')
        form.add_error('code', 'No repair ticket with that code.')
    return render(request, 'repairs/ticket-search.html', {'form': form})


class ReceivedTicketListView(ListView):
    queryset = RepairTicket.objects.filter(status__exact=StatusChoices.RECEIVED).select_related('item')
    context_object_name = 'tickets'
    template_name = 'repairs/ticket-list.html'
    paginate_by = 3

class InProgressTicketListView(ListView):
    queryset = RepairTicket.objects.filter(status__exact=StatusChoices.IN_PROGRESS).select_related('item')
    context_object_name = 'tickets'
    template_name = 'repairs/ticket-list.html'

class FinishedTicketListView(ListView):
    queryset = (RepairTicket.objects.filter(
        status__in=(StatusChoices.FIXED, StatusChoices.UNFIXABLE)
    ).select_related('item'))
    context_object_name = 'tickets'
    template_name = 'repairs/ticket-list.html'
