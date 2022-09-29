from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name =  request.POST['firstname']
        last_name =  request.POST['lastname']
        email = request.POST['email']
        password  = request.POST['password']
        password2  = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
                user.save()
                
                user_login = auth.authenticate(username=username,password=password)
                auth.login(request, user_login)
                
                user_model = User.objects.get(username=username)
                profile = Profile.objects.create(user=user_model)
                profile.save()
                return redirect('index')
        else:
            messages.info(request, 'Password does not match')
            return redirect('index')
        
    return render(request,'signup.html')

def signout(request):
    return render(request,'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        print(email)
        print(password)
        user = auth.authenticate(email=email,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')
    return render(request,'signin.html')
def signout(request):
    auth.logout(request)
    return redirect('signin')
   