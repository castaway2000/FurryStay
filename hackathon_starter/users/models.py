from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class ModelManager(models.Manager, UserID=None):
#     self.userid = self.UserID
#     def get_queryset(self, userid):
#         if self.userid != None:
            
#         return super(ModelManager, self).get_queryset().filter(user_id=userid)


class Profile(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(User)
    oauth_token = models.CharField(max_length=200)
    oauth_secret = models.CharField(max_length=200)
    def __unicode__(self):
        return unicode(self.user)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    class Meta:
        ordering = ('created',)
        

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    objects = models.Manager()
    user = models.OneToOneField(User)
    profile_image = models.ImageField(upload_to='img/userpics/', default='img/userpics/default_profile_picture.jpg')
    interests = models.CharField(max_length=500)
    accomodation = models.CharField(max_length=500)
    twitter = models.CharField(max_length=255)
    facebook = models.CharField(max_length=255)
    telegram = models.CharField(max_length=255)
    about = models.CharField(max_length=5000)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class HostRegistration(models.Model):
    objects = models.Manager()
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=15)
    country = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user


class Reviews(models.Model):
    objects = models.Manager()
    to_user = models.ForeignKey(User, related_name='to_user')
    from_user = models.OneToOneField(User, related_name='from_user')
    rating = models.CharField(max_length=1)
    review = models.CharField(max_length=1000)
    

class DirectMessage(models.Model):
    objects = models.Manager()
    to_user = models.ForeignKey(User, related_name='recv_user')
    from_user = models.OneToOneField(User, related_name='sender_user')
    message = models.CharField(max_length=5000)
    created = models.DateTimeField(max_length=120)