from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def auth_register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if CustomUser.objects.filter(username=username).exists():
            # Display an error message if the team name is already taken
            messages.warning(request,'username is taken')
            return redirect('register')
        elif password1 != password2:
            messages.error(request,'both passwords are different')
            return redirect('register')
        else:
            # Create a new Team
            user = CustomUser.objects.create_user(
                username=username,email=email,password=password1
            )
            messages.success(request,'User created successfully')
            return redirect('login')
    return render(request,'register.html')

def auth_logout(request):
    logout(request)
    return redirect('login')