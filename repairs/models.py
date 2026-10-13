import uuid
from django.db import models

from volunteers.models import Repairer


class StatusChoices(models.TextChoices):
    RECEIVED = 'received', 'received'
    IN_PROGRESS = 'in-progress', 'in-progress'
    FIXED = 'fixed', 'fixed'
    UNFIXABLE = 'unfixable', 'unfixable'

class RepairTicket(models.Model):
    code = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )

    item = models.ForeignKey(
        to='Item',
        on_delete=models.CASCADE,
    )

    serial_number = models.TextField(
        max_length=30,
    )

    status = models.TextField(
        choices=StatusChoices.choices,
        default=StatusChoices.RECEIVED,
    )

    repairers = models.ManyToManyField(
        to=Repairer,

    )

    def __str__(self):
        return f"{self.item.brand}, SN:{self.serial_number}, owner:{self.item.owner_name} ({self.status})"