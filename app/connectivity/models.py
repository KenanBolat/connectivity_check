from django.db import models


class Connectivity(models.Model):
    IP = models.CharField(max_length=100)
    description = models.
    is_accessible = models.BooleanField(default=False)
    is_enabled = models.BooleanField(default=False)
    update_date = models.DateTimeField()

    def __str__(self):
        return self.IP
