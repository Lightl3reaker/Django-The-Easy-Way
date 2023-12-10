from django.db import models

# Create your models here.

class Flower(models.Model):
    title=models.CharField(max_length=255,default='')
    description=models.TextField(default='')
    def __str__(self):
        return self.title