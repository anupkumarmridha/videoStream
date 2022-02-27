from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from home.validators import file_size
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("homeView")

class Video(models.Model):
    title=models.CharField(max_length=255)
    video=models.FileField(upload_to="video_to/%y")
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.CharField(max_length=255)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + '|' + str( self.author)

    def get_absolute_url(self):
        return reverse('homeView')

class Comment(models.Model):
    video=models.ForeignKey(Video, related_name="comments", on_delete=models.CASCADE)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=models.TextField()
    parrent=models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at=models.DateTimeField(auto_now_add=True)