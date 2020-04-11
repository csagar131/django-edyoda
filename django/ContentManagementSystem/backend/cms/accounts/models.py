from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length = 500,blank = True)
    image =  models.ImageField(upload_to ='profiles/',blank = True)
    slug = models.SlugField(blank = True)


    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('profile',kwargs = {'slug':self.slug})
    