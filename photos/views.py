from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image, Profile, Comments, Followers
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def home(request):
    current_user=request.user.id
    images = Image.all_images()
    profile_image=Profile.objects.filter(userId=current_user)
    profile=profile_image.reverse()[0:1]
    comments=Comments.objects.all()
    users=User.objects.all().exclude(id=request.user.id)
    row = round(len(images)/4)
    images1 = Image.all_images()[0:row]
    images2 = Image.all_images()[row:row*2]
    images3 = Image.all_images()[row*2:row*3]
    images4 = Image.all_images()[row*3:row*4]
    return render(request, 'home.html', {"images": images, "images1": images1, "images2": images2, "images3": images3, "images4": images4,"profile":profile,"users":users,"comments":comments})

@login_required(login_url='/accounts/login/')
def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.save()
        return redirect('home')

    else:
        form = NewImageForm()
    return render(request, 'upload.html', {"form": form})

@login_required(login_url="/accounts/login/")
def myprofile(request):
    try:
        current_user=request.user.id
        profile_photos=Image.objects.filter(userId=current_user)
        profile_image=Profile.objects.filter(userId=current_user).all()
        profile=profile_image.reverse()[0:1]

    except Exception as e:
        raise Http404()

    return render(request,"profile.html",{'profile':profile_photos,"pic":profile})

@login_required(login_url="/accounts/login/")
def edit(request):
    current_user_id=request.user.id
    profile=Profile.objects.filter(userId=current_user_id)
    if len(profile)<1:

        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES)
            if form.is_valid():
                profile=form.save(commit=False)
                profile.userId=current_user_id
                profile.save()
            return redirect("profile")
        else:
            form=EditProfile()
            return render(request,"edit.html",{"form":form})
    else:
        if request.method=='POST':
            form=EditProfile(request.POST,request.FILES )
            if form.is_valid():
                profile=form.save(commit=False)
                bio=form.cleaned_data['bio']
                pic=form.cleaned_data['profilepic']
                update=Profile.objects.filter(userId=current_user_id).update(bio=bio,profilepic=profilepic)
                profile.userId=current_user_id
                profile.save(update)
            return redirect("profile")
        else:

            form=EditProfile()

            return render(request,"edit.html",{"form":form})

@login_required(login_url="/accounts/login/")
def profile(request):
    pass

@login_required(login_url="/accounts/login/")
def search(request):
    pass