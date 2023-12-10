from django.contrib import admin
from myapp.models import Flower,Tag

# Register your models here.
admin.site.register(Flower)
admin.site.register(Tag)