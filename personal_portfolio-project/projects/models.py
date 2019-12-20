from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField(default='') 
    technology = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    link = models.URLField(max_length=200,default='')
    code = models.BooleanField(default=True)
