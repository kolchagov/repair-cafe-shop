from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ItemForm
from catalog.models import Item
from repairs.models import RepairTicket, StatusChoices


class CatalogItemListView(ListView):
    model = Item


class CatalogItemDetailView(DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['open_ticket'] = self.object.repair_tickets.filter(
            status__in=(StatusChoices.RECEIVED, StatusChoices.IN_PROGRESS)
        ).order_by('-updated_at').first()
        return context


class CatalogItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/add-item.html'


class CatalogItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/edit-item.html'

class CatalogDeleteView(DeleteView):
    model = Item
    template_name = 'catalog/delete-item.html'

    success_url = reverse_lazy('catalog:list')