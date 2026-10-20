from django import forms

from catalog.models import Category, Item
from repair_cafe_shop.forms import BootstrapForm


class CategoryForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Category name',
            'description': 'Description',
        }
        help_texts = {
            'name': 'A short, unique name, e.g. "Coffee machines".',
            'description': 'What kinds of items belong in this category?',
        }
        error_messages = {
            'name': {
                'required': 'Please give the category a name.',
                'unique': 'A category with this name already exists.',
            },
            'description': {
                'required': 'Please describe the category.',
            },
        }

class ItemForm(BootstrapForm, forms.ModelForm):
    class Meta:
        model = Item
        fields = ['owner_name', 'category', 'brand', 'problem_description', 'photo']
        labels = {
            'owner_name': 'Owner',
            'brand': 'Brand / model',
            'problem_description': 'What is wrong?',
            'photo': 'Photo',
        }
        help_texts = {
            'problem_description': 'Describe the fault in at least four words.',
            'photo': 'Optional photo of the item.',
        }
        widgets = {
            'owner_name': forms.TextInput(attrs={'placeholder': 'e.g. Jane Doe'}),
            'brand': forms.TextInput(attrs={'placeholder': 'e.g. DeLonghi EC155'}),
            'problem_description': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'e.g. Pump makes a loud noise and no water comes out',
            }),
        }
        error_messages = {
            'owner_name': {'required': "Please enter the owner's name."},
            'category': {'required': 'Please choose a category.'},
            'brand': {'required': 'Please enter the brand or model.'},
            'problem_description': {'required': 'Please describe the problem.'},
        }
