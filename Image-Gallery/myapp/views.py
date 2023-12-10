from django.shortcuts import render
from myapp.models import Flower

# Create your views here.
def index(request):
    flowers=Flower.objects.all()
    return render(request,'myapp/index.html',{'flowers':flowers})