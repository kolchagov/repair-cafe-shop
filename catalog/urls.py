from django.urls import path

from catalog.views import ModelListView

urlpatterns = [
    path('', ModelListView.as_view(), name='items-list'),
]