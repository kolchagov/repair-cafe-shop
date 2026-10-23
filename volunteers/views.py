from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from volunteers.forms import RepairerForm
from volunteers.models import Repairer


class RepairerDetailsView(DetailView):
    model = Repairer
    template_name = 'volunteers/repairer-detail.html'
    context_object_name = 'repairer'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # disabled fields render the values read-only, but still as widgets
        form = RepairerForm(instance=self.object)
        for field in form.fields.values():
            field.disabled = True
        context['form'] = form
        return context


class RepairerListView(ListView):
    template_name = 'volunteers/repairer-list.html'

    paginate_by = 3

    def get_queryset(self):
        return Repairer.objects.all()


class RepairerCreateView(CreateView):
    model = Repairer
    template_name = 'volunteers/repairer-edit.html'
    form_class = RepairerForm

    def get_success_url(self):
        return reverse('volunteers:list')


class RepairerUpdateView(UpdateView):
    model = Repairer
    form_class = RepairerForm
    template_name = 'volunteers/repairer-edit.html'
    success_url = reverse_lazy('volunteers:list')


class RepairerDeleteView(DeleteView):
    model = Repairer
    template_name = 'volunteers/repairer-delete.html'
    success_url = reverse_lazy('volunteers:list')
