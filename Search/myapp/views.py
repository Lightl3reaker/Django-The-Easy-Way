from django.shortcuts import render
from myapp.models import Flower,Tag

# Create your views here.
def index(request):
    q=request.GET.get('q',None)
    items=''
    if q is None or q is '':
        flowers=Flower.objects.all()
    elif q is not None:
        flowers=Flower.objects.filter(title__contains=q)
    return render(request,'myapp/index.html',{'flowers':flowers})
def tags(request,slug=None):
    flowers=Flower.objects.filter(tags__slug=slug).values()
    return render(request,'myapp/index.html',{'flowers':flowers})