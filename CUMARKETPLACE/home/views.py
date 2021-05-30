from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings

from django import forms

from .models import ProductInfo
from .forms import CreateUserForm
from .forms import ImageForm


# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')

    return render(request,'index.html')

def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            
            return redirect("/")
        else:
            messages.success(request, "Wrong Username or Password")
            return render(request,'login.html')
    return render(request,'login.html')

def signupuser(request):

    form = CreateUserForm()
    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
           form.save()
           user= form.cleaned_data.get('username')
           messages.success(request, "Account was created for "+ user)
           return redirect('login')
    
    context = {'form': form}

    return render(request,'signup.html',context)

def product_reg(request):
    if request.method == 'POST':
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            file_url=form.instance
            messages.success(request, "Product was successfully added to the database ")
            return redirect('/product_reg',{'file_url':file_url})

        
    else:
        form=ImageForm()
        
    return render(request,'product_reg.html',{'form':form})

def product_sell(request):
    if ProductInfo.objects.count()==0:
        messages.success(request, "There are no products available at the moment")
    if request.method == 'POST':
        search = request.POST.get('search')
        products = ProductInfo.objects.filter(itemname__startswith = search)
        if products.exists()==False:
            messages.success(request, "No products found ")
    else:
        products = ProductInfo.objects.all()

    return render(request,'product_sell.html',{'products':products})

def product_conf(request,primarykey):
    product=ProductInfo.objects.get(primarykey=primarykey)
    name=product.itemname
    sellername=product.sellername
    selleremail=product.email
    address=product.address
    price=product.price

    current_user=request.user
    buyeremail=current_user.email
    buyername=current_user.first_name+' '+current_user.last_name

    if request.method == 'POST':

        product.delete()   
        send_mail('Product seller Information', 'The name of the seller is '+sellername+' product is '+name+' \nThe email of the seller is '+selleremail+'. the current address of the seller is :'+address+
        '\nYou have agreed to buy the item at a price of '+price+'.\nFor more Information you can contact the seller from the given email address.','EMAIL_HOST_USER', [buyeremail])
        print(buyeremail)
        send_mail('Buy Request from '+buyername,'Your product has receiver a buy request from '+buyername+
        '\n So he might try to contact you using your email please check your email regularly to not miss the selling apportunity','EMAIL_HOST_USER', [selleremail])
    return render(request,'emailsent2.html')

def emailsent(request):


    return render(request,'emailsent.html')

def contactus(request):

    return render(request,'contactus.html')


def aboutus(request):

    return render(request,'aboutus.html')

def logoutuser(request):
    logout(request)
    return redirect("/login")
