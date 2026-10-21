from django.urls import path

from repairs.views import RepairTicketDetailView, ticket_lookup

app_name = 'repairs'

urlpatterns = [
    path('', ticket_lookup, name='lookup'),
    path('<uuid:code>/details', RepairTicketDetailView.as_view(), name='details'),
]
