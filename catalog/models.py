from django.core.validators import RegexValidator, MinLengthValidator
from django.db import models
from django.urls import reverse


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
        validators=[
            RegexValidator(
                r'^\W*(?:\w+\W+)\w+\W*$',
                message='At least two names required'
            )
        ]
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='items',
    )
    brand = models.CharField(
        max_length=100,
    )

    serial_number = models.TextField(
        max_length=30,
        validators=[
            MinLengthValidator(3, "Serial number is required, minimum 3 chars"),
        ]
    )

    problem_description = models.TextField(
        validators=[
            RegexValidator(
                regex=r'^\W*(?:\w+\W+){3,}\w+\W*$',
                message='Give meaningful problem description. At least four words required.',
            )
        ]
    )
    # optional
    photo = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.owner_name}, {self.brand} - {self.category}"

    def get_absolute_url(self):
        return reverse('catalog:details', args=[str(self.pk)])