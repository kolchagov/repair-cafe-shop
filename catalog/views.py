from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ItemForm, CategoryForm
from catalog.models import Item, Category
from repairs.models import RepairTicket, StatusChoices


class CatalogItemListView(ListView):
    model = Item
    template_name = "catalog/item-list.html"
    paginate_by = 3


class CatalogItemDetailView(DetailView):
    model = Item
    template_name = "catalog/item-detail.html"

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

    def get_success_url(self):
        # create new repair ticket when new item is added
        RepairTicket.objects.create(item=self.object, status=StatusChoices.RECEIVED)
        return reverse('catalog:details', kwargs={'pk': self.object.pk})


class CatalogItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'catalog/edit-item.html'


class CatalogDeleteView(DeleteView):
    model = Item
    template_name = 'catalog/delete-item.html'

    success_url = reverse_lazy('catalog:list')


class CategoryListView(ListView):
    model = Category
    template_name = "catalog/category-list.html"
    paginate_by = 3


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/add-category.html'

    def get_success_url(self):
        return reverse('catalog:category-list')


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'catalog/delete-category.html'

    success_url = reverse_lazy('catalog:category-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'catalog/edit-category.html'

    def get_success_url(self):
        return reverse('catalog:category-list')
