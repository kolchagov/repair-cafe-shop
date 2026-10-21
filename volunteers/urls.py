from django.urls import path, include
from volunteers.views import (
    RepairerListView,
    RepairerDetailsView,
    RepairerUpdateView,
    RepairerDeleteView, RepairerCreateView,
)


app_name = 'volunteers'

urlpatterns = [
    path('', RepairerListView.as_view(), name='list'),
    path('add/', RepairerCreateView.as_view(), name='add'),
    path('<int:pk>/', include([
        path('details', RepairerDetailsView.as_view(), name='details'),
        path('edit', RepairerUpdateView.as_view(), name='edit'),
        path('delete', RepairerDeleteView.as_view(), name='delete'),
    ])),
]
