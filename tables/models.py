import uuid

from django.db import models
from django.utils import timezone


class TableBrand(models.Model):
    name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Table(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    url = models.CharField(max_length=2048, default='Unknown')
    created_date = models.DateField(default=timezone.now)
    brand = models.ForeignKey(TableBrand, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


