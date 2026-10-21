from django.db.models import Count, Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import Item
from repairs.models import RepairTicket, StatusChoices


def dashboard_view(request: HttpRequest) -> HttpResponse:
    stats = RepairTicket.objects.aggregate(
        received=Count('pk', filter=Q(status=StatusChoices.RECEIVED)),
        in_progress=Count('pk', filter=Q(status=StatusChoices.IN_PROGRESS)),
        fixed=Count('pk', filter=Q(status=StatusChoices.FIXED)),
        unfixable=Count('pk', filter=Q(status=StatusChoices.UNFIXABLE)),
    )
    # success rate is measured against tickets that reached a final verdict
    closed = stats['fixed'] + stats['unfixable']

    context = {
        **stats,
        'waiting': stats['received'] + stats['in_progress'],
        'customers_count': Item.objects.values('owner_name').distinct().count(),
        'items_count': Item.objects.count(),
        'success_rate': round(stats['fixed'] * 100 / closed) if closed else 0,
    }
    return render(request, 'dashboard.html', context)
