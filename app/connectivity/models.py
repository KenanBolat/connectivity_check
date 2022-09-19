from django.db import models
from django.db.models import Count, F, Value

import datetime


class ConnectivityManager(models.Manager):
    def update_counter(self, pk):
        self.filter(id=pk).update(count=F('count') + 1)


class Connectivity(models.Model):
    ip = models.GenericIPAddressField(unique=True)
    description = models.CharField(max_length=255)
    is_accessible = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(default=datetime.datetime.now())
    update_counter = models.PositiveIntegerField(default=0)
    objects = ConnectivityManager()

    def __str__(self):
        return self.IP
