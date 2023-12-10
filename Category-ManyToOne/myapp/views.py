from django.shortcuts import render
from django.shortcuts import get_object_or_404
from myapp.models import Flower

# Create your views here.
def index(request):
    flowers=Flower.objects.all()
    return render(request,'myapp/index.html',{'flowers':flowers})

def detail(request,slug=None):
    flower=get_object_or_404(Flower,slug=slug)
    return render(request,'myapp/detail.html',{'flower':flower})