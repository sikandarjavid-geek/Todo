from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tasks(models.Model):
    title = models.CharField(max_length=200)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#Create UserProfile Model
class UserProfileModel(models.Model):
    #Creating One to One Relationship
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    #Additional Attributes

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

     
