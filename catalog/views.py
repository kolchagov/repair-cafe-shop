from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ItemForm
from catalog.models import Item


class CatalogItemListView(ListView):
    model = Item


class CatalogItemDetailView(DetailView):
    model = Item


class CatalogItemCreateView(CreateView):
    model = Item
    form_class = ItemForm


class CatalogItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/edit-item.html'

class CatalogDeleteView(DeleteView):
    model = Item
    template_name = 'catalog/delete-item.html'

    success_url = reverse_lazy('catalog:list')