from django.core.validators import RegexValidator
from django.db import models

class RepairSkills(models.TextChoices):
    MECHANIC = "MECHANIC", "MECHANIC"
    ELECTRIC = "ELECTRIC", "ELECTRIC"
    MAINTENANCE = "MAINTENANCE", "MAINTENANCE"
    CLEANING = "CLEANING", "CLEANING"

class Repairer(models.Model):
    name = models.CharField(
        max_length=100
    )
    skills = models.CharField(
        max_length=100,
        choices=RepairSkills.choices,
    )

    phone = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r"^\+?1?\d{9,15}$",
                message="Phone number must be entered in the format: '+999999999', up to 15 digits",
            )
        ]
    )

    email = models.EmailField(
        max_length=100,
        null=True,
        blank=True,
    )

    notes = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        skills = self.skills.split(",")
        return f"{self.name}, {self.phone} ({skills})"
