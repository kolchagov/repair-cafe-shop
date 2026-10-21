import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone

from catalog.models import Item
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
        to=Item,
        on_delete=models.CASCADE,
        related_name='repair_tickets',
    )

    status = models.TextField(
        choices=StatusChoices.choices,
        default=StatusChoices.RECEIVED,
    )

    repairers = models.ManyToManyField(
        to=Repairer,
    )

    diagnosis = models.TextField(
        null=True,
        blank=True,
    )

    spare_parts_cost = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[
            MinValueValidator(0)
        ],
        null=True,
        blank=True,
    )

    intake_date = models.DateField(
        default=timezone.localdate,
        validators=[
            MaxValueValidator(
                timezone.localdate,
                message='Intake date cannot be in the future.',
            )
        ],
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item.brand}, SN:{self.item.serial_number}, owner:{self.item.owner_name} ({self.status})"
