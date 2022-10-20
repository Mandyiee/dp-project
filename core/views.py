from django.shortcuts import render, redirect
from .models import Flier, Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json, base64
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from html2image import Html2Image
hti = Html2Image()
# Create your views here.

@login_required(login_url='accounts/login')
def index(request):
    fliers = Flier.objects.order_by('-no_of_clicks')
    context = {
        'fliers':fliers
    }
    return render(request,'index.html',context)

@login_required(login_url='accounts/login')
def create(request):
    return render(request,'create.html')

@login_required(login_url='accounts/login')
def alldp(request):
    return render(request,'alldp.html')

@login_required(login_url='accounts/login')
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='accounts/login')
def publish(request):
    if request.method == 'POST':
        user  = User.objects.get(username = request.user.username)
        flier_obj = json.loads(request.POST['flier'])
        #print(flier_obj)
        #print(type(flier_obj))
        event_name = flier_obj['event_name']
        description = flier_obj['description']
        hashtag1 = flier_obj['hashtag1']
        hashtag2 = flier_obj['hashtag2']
        htmlFile = flier_obj['htmlFile']
        imageString = flier_obj['file']
        
        flier, created = Flier.objects.get_or_create(user=user,event_name=event_name,description=description,hashtag1=hashtag1,hashtag2=hashtag2,htmlFile=htmlFile,imageString=imageString)
        flier.save()
        return redirect('visitor1/' + str(flier.id))
    return render(request,'publish.html')

@login_required(login_url='accounts/login')
def preview(request):
    return render(request,'preview.html')

@login_required(login_url='accounts/login')
def avatar(request):
    return render(request,'avatar.html')

@login_required(login_url='accounts/login')
def visitor1(request,pk):
    user = User.objects.get(username = request.user.username)
    flier = Flier.objects.get(id=pk)
    flier.no_of_clicks += 1
    flier.save()
    if request.method == 'POST':
        attendee_name = request.POST['attendee_name']
        attendee_htmlValue = request.POST['htmlValue']
        attendee_b64Value = request.POST['b64Value']
        
        data = hti.screenshot(html_str=attendee_htmlValue,css_file='./static/css/index.css')
        print(data)
        flier.image = data 
        
    return render(request,'visitor1.html',{'flier':flier})

@login_required(login_url='accounts/login')
def visitor2(request,pk):
    return render(request,'visitor2.html')