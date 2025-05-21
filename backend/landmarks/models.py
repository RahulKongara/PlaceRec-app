from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Landmark(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="landmarks/")
    embedding = models.JSONField()
    
    def __str__(self):
        return self.name