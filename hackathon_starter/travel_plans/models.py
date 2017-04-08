from django.db import models
from django.contrib.auth.models import User
from users.models import HostRegistration


class LocationVisit(models.Model):
    user = models.ForeignKey(User)
    location = models.ForeignKey(HostRegistration, on_delete=models.CASCADE)
    date_start = models.DateField()
    date_end = models.DateField()

    def __unicode__(self):
        return "%s, %s" % (unicode(self.user), self.location.city)