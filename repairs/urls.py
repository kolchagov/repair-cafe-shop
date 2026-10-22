from django.urls import path, include

from repairs.views import RepairTicketDetailView, ticket_lookup, RepairTicketEditView, ReceivedTicketListView, \
    FinishedTicketListView, InProgressTicketListView

app_name = 'repairs'

urlpatterns = [
    path('', ticket_lookup, name='lookup'),
    path('pending-tickets/', ReceivedTicketListView.as_view(), name='pending-tickets'),
    path('in-progress-tickets/', InProgressTicketListView.as_view(), name='in-progress-tickets'),
    path('finished-tickets/', FinishedTicketListView.as_view(), name='finished-tickets'),
    path('<uuid:code>/', include([
        path("details", RepairTicketDetailView.as_view(), name='details'),
        path("begin-repair/", RepairTicketEditView.as_view(), name='begin-repair'),
    ])),
    path('edit', RepairTicketEditView.as_view(), name='edit'),
]
