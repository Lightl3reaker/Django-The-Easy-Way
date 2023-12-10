from django import forms
from django.forms import ModelForm
from myapp.models import Flower

#creating a ModelForm
#a ModelForm is a form created Directly from a Model
class MyForm(ModelForm):#{{form}} will call this
    title=forms.CharField(
        label="Title",
        widget=forms.TextInput(#this returns html form field
            attrs={'class':'form-control'}#<input type="text" class="form-control">        )
        )
    )
    description=forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={'class':'form-control'}
            )
    )
    #specifying which model is converted into form
    class Meta:
        model=Flower#here is the Flower model
        fields=['title','description']#this is where the data pass to db model