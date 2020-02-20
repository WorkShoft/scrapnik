import uuid
from django.db import models


class Table(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=1000)
    created_date = models.DateField()

    def __str__(self):
        return self.name
    
