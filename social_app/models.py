from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_user_directory, default = get_default_image)
    institute = models.CharField(max_length=60)
    age = models.IntegerField(default=-1)
    bio = models.TextField(max_length=150)

def get_user_directory()