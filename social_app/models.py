from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime
# Create your models here.
def get_user_image(instance,filename):
    return 'files/{0}/avatar/{1}'.format(instance.user.username, filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=get_user_image, default = 'files/default_avatar.jpg')
    institute = models.CharField(max_length=60)
    age = models.IntegerField(default=-1)
    bio = models.TextField(max_length=150)


@receiver(post_save, sender=User, dispatch_uid = 'save_new_user_profile')
def create_user_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile.objects.create(user = instance)
        profile.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def get_user_post_dir(instance, filename):
    return 'files/{0}/posts/{1}'.format(instance.user.username, filename)

def get_user_output_files(instance, filename):
    return 'files/{0}/videos/{1}'.format(instance.user.username, filename)

class Post(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'posts')
    title = models.CharField(max_length=70)
    description = models.TextField(max_length = 500)
    input_file = models.FileField(upload_to = get_user_post_dir)
    output_file = models.FileField(upload_to = get_user_post_dir, null=True)
    created_at = models.DateTimeField()
    likes = models.IntegerField(null = True)
    updated_at = models.DateTimeField(blank = True, null=True)
    published_date = models.DateTimeField(blank = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey("social_app.Post", on_delete=models.CASCADE, related_name = 'comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'user_comments')
    text = models.CharField(max_length = 750)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.author.username + '-' + str(datetime.now().date()) + '-' + self.post.id