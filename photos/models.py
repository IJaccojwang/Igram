from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    '''
    image Class for all images added to the app
    '''
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=300, blank = True)
    post_date = models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)
    userId=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-post_date']
    
    def save_image(self):
        '''
        Method to save new images
        '''
        self.save()
    
    def delete_image(self):
        '''
        Method to delete images
        '''
        self.delete()
    
    @classmethod
    def all_images(cls):
        '''
        Method to view all images
        '''
        images = cls.objects.all()
        return images

class Comments(models.Model):
    comment=models.TextField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    images=models.IntegerField()

class Followers(models.Model):
    user=models.CharField(max_length=30)
    insta=models.CharField(default='',max_length=30)
    user_id=models.IntegerField()

class Profile(models.Model):
    profilepic=models.ImageField(upload_to='profile/',blank=True)
    bio=models.CharField(max_length=30)
    userId=models.IntegerField()


    def __str__(self):
        return self.bio

    