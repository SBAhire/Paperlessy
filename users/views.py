from django.shortcuts import render,redirect
from .models import *
from django.http import request,HttpResponse
from .forms import RegistrationForm
from django.contrib import messages
# Create your views here.
def register(request):
    register_form=RegistrationForm()
    if request.method=="POST":
        register_form=RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request,"New user Account Created")
            return redirect('/user/login')
    
    content = {
        'register_form' : register_form,
    }
    return render(request,'users/register.html',content)
