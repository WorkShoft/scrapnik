import uuid

from django.db import models
from django.utils import timezone


class UserAgent(models.Model):
    """
    Most common user agents
    """
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    percent = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    useragent = models.CharField(max_length=256)
    system = models.CharField(max_length=128)
    created_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.useragent
