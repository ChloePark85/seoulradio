from django.db import models

# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=10)
    place=models.TextField()
    title=models.CharField(max_length=30)
    contents=models.TextField()
    tag=models.TextField()
    cdate=models.DateTimeField(auto_now_add=True)
    