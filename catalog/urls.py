from django.urls import path, include

from catalog.views import CatalogItemListView, CatalogItemDetailView, CatalogItemUpdateView, CatalogDeleteView, \
    CatalogItemCreateView

app_name = 'catalog'
urlpatterns = [
    path('', CatalogItemListView.as_view(), name='list'),
    path('add/', CatalogItemCreateView.as_view(), name='add'),
    path('<int:pk>/', include([
        path('details', CatalogItemDetailView.as_view(), name='details'),
        path('edit', CatalogItemUpdateView.as_view(), name='edit'),
        path('delete', CatalogDeleteView.as_view(), name='delete'),
    ])),
]
