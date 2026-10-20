from django import forms

from repair_cafe_shop.forms import BootstrapForm
from repairs.models import RepairTicket


class RepairTicketForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = RepairTicket
        fields = [
            'item',
            'serial_number',
            'status',
            'intake_date',
            'repairers',
            'diagnosis',
            'spare_parts_cost',
        ]
        labels = {
            'serial_number': 'Serial number',
            'intake_date': 'Intake date',
            'spare_parts_cost': 'Spare parts cost',
            'repairers': 'Repairers',
            'diagnosis': 'Diagnosis',
        }
        help_texts = {
            'diagnosis': 'Diagnosed problems',
            'serial_number': 'Serial number printed on the item.',
            'intake_date': 'When the item was brought in; cannot be in the future.',
            'spare_parts_cost': 'Estimated cost of spare parts, 0 or more.',
            'repairers': 'Hold Ctrl/Cmd to select more than one.',
        }
        widgets = {
            'serial_number': forms.TextInput(
                attrs={'placeholder': 'e.g. SN12345'}
            ),
            'intake_date': forms.DateInput(
                attrs={'type': 'date'},
            ),
            'diagnosis': forms.Textarea(
                attrs={'placeholder': 'Found problems description'}
            ),
        }
        error_messages = {
            'item': {'required': 'Please choose the item being repaired.'},
            'serial_number': {'required': 'Please enter the serial number.'},
            'status': {'required': 'Please choose a status.'},
            'intake_date': {'required': 'Please enter the intake date.'},
            'spare_parts_cost': {'required': 'Please enter the estimated cost (0 is allowed).'},
        }
