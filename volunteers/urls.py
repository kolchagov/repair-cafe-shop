from django.urls import path, include
from volunteers.views import (
    RepairerListView,
    RepairerDetailsView,
    RepairerUpdateView,
    RepairerDeleteView,
)


app_name = 'volunteers'

urlpatterns = [
    path('', RepairerListView.as_view(), name='list'),
    path('<int:pk>/', include([
        path('details', RepairerDetailsView.as_view(), name='details'),
        path('edit', RepairerUpdateView.as_view(), name='edit'),
        path('delete', RepairerDeleteView.as_view(), name='delete'),
    ])),
]
