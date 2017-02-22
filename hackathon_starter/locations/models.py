from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=256)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name