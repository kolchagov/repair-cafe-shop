from django import forms
from django.forms import Form


class BootstrapForm(Form):
    """Mixin BSForm: Adds Bootstrap classes and styling to every widget on a form."""

    template_name = 'bs5/form.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            # check for <select> widgets and apply proper styling
            if isinstance(field.widget, (forms.Select, forms.SelectMultiple)):
                css = 'form-select'
            else:
                css = 'form-control'
            field.widget.attrs.setdefault('class', css)
        for name in self.errors:
            if name in self.fields:
                widget = self.fields[name].widget
                widget.attrs['class'] += ' is-invalid'
