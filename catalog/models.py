from django.core.validators import RegexValidator
from django.db import models


class Category(models.Model):
    """
    Category model, describes different categories of coffe machines
    """
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.name}: {self.description}"

    class Meta:
        ordering = ['name']


class Item(models.Model):
    """
    Item model describing items to be repaired
    """
    owner_name = models.CharField(
        max_length=100,
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='items',
    )
    brand = models.CharField(
        max_length=100,
    )
    problem_description = models.TextField(
        validators=[
            RegexValidator(
                regex='^\w+(?: \w+){3,}$',
                message='Give meaningful problem description. At least four words required.',
            )
        ]
    )
    photo = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.owner_name}, {self.brand} {self.category}: {self.problem_description})"