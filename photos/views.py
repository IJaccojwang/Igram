from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image
from django.contrib.auth.decorators import login_required
from .forms import NewImageForm

@login_required(login_url='/accounts/login/')
def home(request):
    images = Image.all_images()
    row = round(len(images)/4)
    images1 = Image.all_images()[0:row]
    images2 = Image.all_images()[row:row*2]
    images3 = Image.all_images()[row*2:row*3]
    images4 = Image.all_images()[row*3:row*4]
    return render(request, 'home.html', {"images": images, "images1": images1, "images2": images2, "images3": images3, "images4": images4})

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