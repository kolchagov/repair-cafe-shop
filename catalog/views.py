
from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Category, Item


class ModelListView(ListView):
    model = Item
