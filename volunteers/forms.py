from django import forms

from repair_cafe_shop.forms import BootstrapForm
from volunteers.models import Repairer


class RepairerForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Repairer
        fields = ['name', 'skills', 'phone', 'email', 'notes']
        labels = {
            'name': 'Full name',
            'skills': 'Main skill',
            'phone': 'Phone number',
            'email': 'Email',
            'notes': 'Notes',
        }
        help_texts = {
            'phone': "Format: '+999999999' or '0999999999', up to 15 digits.",
            'notes': 'Optional short availability notes.',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'Ivan Ivanov'}
            ),
            'phone': forms.TextInput(
                attrs={'placeholder': '0881234567'}
            ),
            'notes': forms.Textarea(
                attrs={'rows': 2, 'placeholder': 'Optional'}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': 'user@domain.com, optional'}
            )
        }
        error_messages = {
            'name': {'required': "Please enter the repairer's name."},
            'skills': {'required': 'Please choose a skill.'},
            'phone': {'required': 'Please enter a phone number.'},
        }
