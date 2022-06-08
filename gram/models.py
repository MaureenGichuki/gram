from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True,upload_to = 'profiles/')
    bio = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.user.username}'

    def profile(self):
        self.save()

class Post(models.Model):
    pic = models.ImageField(blank=True, upload_to = 'pics/')
    caption = models.CharField(blank=True,max_length = 255)
    like = models.IntegerField(default=0)
    comments = models.CharField(blank=True,max_length = 255)

    def __str__(self):
        return f'{self.profile.user.username}'
    
    def post(self):
        self.save()

class Following(models.Model):
    username = models.CharField(blank=True,max_length = 255)
    followed = models.CharField(blank=True,max_length = 255)

    def __str__(self):
        return f'{self.username}'

    def following(self):
        self.save()

class Comment(models.Model):
    post = models.IntegerField(default=0)
    username = models.CharField(blank=True,max_length = 255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.username}'

    def comment_save(self):
        self.save()