
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#blogcreation


class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    content=models.TextField()
    image=models.ImageField(upload_to='images/',blank=True)
    video=models.FileField(upload_to='videos/',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)


def _str_(self):
        return self.title