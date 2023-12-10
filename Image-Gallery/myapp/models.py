from django.db import models

# Create your models here.

class Flower(models.Model):
    title=models.CharField(max_length=255,default='')
    description=models.TextField(default='')
    image=models.ImageField(default='',blank=True,upload_to='images')
    def __str__(self):
        return self.title