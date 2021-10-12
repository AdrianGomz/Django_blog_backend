from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    followers_count = models.IntegerField(default=0)
    followers = models.ManyToManyField(User,related_name='following', blank = True)
    def __str__(self):
        return self.user.username
