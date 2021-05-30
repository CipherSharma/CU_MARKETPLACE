from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import ProductInfo
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    username= forms.CharField(label='UID')
    class Meta:
        model=User
        fields=('first_name','last_name', 'username','email','password1','password2')

class ImageForm(forms.ModelForm):

    class Meta:
        model=ProductInfo
        fields=('sellername','itemname','address','description','email','price','image')

    