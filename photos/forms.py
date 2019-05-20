from .models import Image, Comments, Followers, Profile
from django import forms
from django.forms import ModelForm, Textarea, IntegerField


class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['']

class EditProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['userId']

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        exclude=['user','images']

class Likes(forms.ModelForm):
    class Meta:
        model=Image
        exclude=['likes','comments','date','user','userId','profile','image','name','caption']

class FollowForm(forms.ModelForm):
    class Meta:
        model=Followers
        exclude=['user','insta','user_id']