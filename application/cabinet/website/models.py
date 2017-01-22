from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Staff(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    working_position = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
