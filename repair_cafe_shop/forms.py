from django import forms
from django.forms import Form, ModelForm

from repairs.models import RepairTicket


class BootstrapForm(Form):
    """Mixin BSForm: Adds Bootstrap classes to every widget on a form."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # check for <select> widgets and apply proper styling
            if isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                css = 'form-select'
            else:
                css = 'form-control'
            field.widget.attrs.setdefault('class', css)

class RepairTicketForm(BootstrapForm, ModelForm):
    class Meta:
        model = RepairTicket
        fields = '__all__'