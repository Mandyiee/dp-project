import uuid
import numpy as np
from django.shortcuts import render, redirect
from .models import Category, Flier, Profile, UserFlier
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json, base64, math
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.files.base import ContentFile
from html2image import Html2Image
from PIL import Image, ImageDraw
from io import BytesIO, StringIO
from django.core.files.images import ImageFile
hti = Html2Image()
# Create your views here.

@login_required(login_url='accounts/login')
def index(request):
    fliers = Flier.objects.order_by('-date_created')[:4]
    #fliers = Flier.objects.order_by('-no_of_clicks')
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
        htmlFile = flier_obj['htmlFile']
        imageString = flier_obj['file']
        category = flier_obj['category']
        image_width = flier_obj['image_width']
        image_height = flier_obj['image_height']
        image_top = flier_obj['image_top']
        image_left = flier_obj['image_left']
        
        format, imageString = imageString.split(';base64,') 
        ext = format.split('/')[-1] 

        image = ContentFile(base64.b64decode(imageString), name= event_name + '.' + ext)
        flier, created = Flier.objects.get_or_create(user=user,event_name=event_name,image=image,description=description,hashtag1=hashtag1,htmlFile=htmlFile,imageString=imageString,image_height=image_height,image_left=image_left,image_width=image_width,image_top=image_top)
        categoryModel, created = Category.objects.get_or_create(name=category)
        flier.category.add(categoryModel.id)
        flier.save()
        return redirect('/visitor1/' + str(flier.id))
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
        user = request.POST['attendee_name']
        image = request.FILES.get('attendee_image')
        image_flier = flier.image
        file_name = str(uuid.uuid4())
        path = f"flier-{file_name}.jpeg"
        img_io = BytesIO()
        image1 = Image.open(image_flier).convert("RGB")
 
        image1copy = image1.copy()
        width, height = image1copy.size
        image2 = Image.open(image).convert("RGB")
        imgWidth = int(float(flier.image_width)*width) 
        imgHeight = int(float(flier.image_height)*height)
        imageResize = image2.resize((imgWidth,imgHeight))
        
        height,width = imageResize.size
        lum_img = Image.new('L', [height,width] , 0)
        
        draw = ImageDraw.Draw(lum_img)
        draw.pieslice([(0,0), (height,width)], 0, 360, 
                    fill = 255, outline = "white")
        img_arr =np.array(imageResize)
        lum_img_arr =np.array(lum_img)
        final_img_arr = np.dstack((img_arr,lum_img_arr))
        imageResize2 = Image.fromarray(final_img_arr)
        image2copy = imageResize.copy()
        imgTop =int((int(float(flier.image_left)) * width)/100)
        imgLeft = int((int(float(flier.image_top)) * height)/100)
        image1copy.paste(image2copy, (imgTop,imgLeft))
        image1copy.save(img_io, format='JPEG', quality=100)
        
        
        flier_image = ContentFile(img_io.getvalue(), path)
        userflier = UserFlier.objects.create(flier=flier,user=user,image=image,flier_image=flier_image)
        
        userflier.save()
        return redirect('/visitor2/'+str(userflier.id))
    return render(request,'visitor1.html',{'flier':flier})

@login_required(login_url='accounts/login')
def visitor2(request,pk):
    userflier = UserFlier.objects.get(id=pk)
    print(userflier)
    context = {
        'userflier':userflier
    }
    return render(request,'visitor2.html',context)

@login_required(login_url='accounts/login')
def category(request):
    return render(request,'browse.html')

@login_required(login_url='accounts/login')
def categories(request,cat):
    try:
        category = Category.objects.get(name=cat)
    except ObjectDoesNotExist:
        category = None
    fliers = Flier.objects.filter(category=category)
    
    context = {
        'fliers':fliers
    }
    return render(request,'music.html',context)