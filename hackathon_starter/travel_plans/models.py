from django.db import models
from django.contrib.auth.models import User
from locations.models import Location


class LocationVisit(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(Location)
    date_start = models.DateField()
    date_end = models.DateField()

    def __unicode__(self):
        return "%s, %s" % (unicode(self.user), self.location.name)