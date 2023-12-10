from django.shortcuts import render,get_object_or_404
from .models import Flower
from django.http import HttpResponseRedirect
from .forms import MyForm
from django.contrib.auth.decorators import permission_required

# Create your views here.
def index(request):
    flowers=Flower.objects.all()
    return render(request,'myapp/index.html',{'flowers':flowers})

@permission_required('myapp.add_flower')
def create(request):
    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        form=MyForm()
    return render(request,'myapp/edit.html',{'form':form})

@permission_required('myapp.change_flower')
def edit(request,pk=None):
    flower=get_object_or_404(Flower,pk=pk)
    if request.method=='POST':
        form=MyForm(request.POST,instance=flower)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=MyForm(instance=flower)
    return render(request,'myapp/edit.html',{'form':form})

@permission_required('myapp.delete_flower')
def delete(request,pk=None):
    flower=get_object_or_404(Flower,pk=pk)
    flower.delete()
    flowers=Flower.objects.all()
    return render(request,'myapp/index.html',{"flowers":flowers})