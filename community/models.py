from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Article(models.Model):
    name=models.CharField(max_length=10)
    place=models.CharField(max_length=10)
    title=models.CharField(max_length=30)
    contents=models.TextField()
    tag=models.CharField(max_length=20)
    cdate=models.DateTimeField(auto_now_add=True)

def publish(self):
    self.published_date =timezone.now()
    self.save()

def __str__(self):
    return self.title
    