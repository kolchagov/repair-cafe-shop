from django.urls import path

from repairs.views import RepairTicketDetailView, ticket_lookup, RepairTicketCreateView

app_name = 'repairs'

urlpatterns = [
    path('', ticket_lookup, name='lookup'),
    path('<uuid:code>/details', RepairTicketDetailView.as_view(), name='details'),
    path('add', RepairTicketCreateView.as_view(), name='add'),
]
