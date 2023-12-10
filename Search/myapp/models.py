from django.db import models
from django.utils.text import slugify
# Create your models here.
class Tag(models.Model):
    title=models.CharField(max_length=256,default='')
    slug=models.SlugField(blank=True,default='')
    def __str__(self):
        return self.title
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Tag,self).save()

class Flower(models.Model):
    title=models.CharField(max_length=255,default='')
    description=models.TextField(default='')
    tags=models.ManyToManyField(Tag)
    slug=models.SlugField(blank=True,default='')
    def __str__(self):
        return self.title
    def save(self,*args, **kwargs):
        self.slug=self.title
        super(Flower,self).save()