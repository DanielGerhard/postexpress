from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description
    
class AppImgs(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=55, blank=True)
    image = models.ImageField(blank=True, upload_to='images/%Y/%m/')
