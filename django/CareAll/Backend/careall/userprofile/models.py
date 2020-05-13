from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    email = models.EmailField()
    is_elder = models.BooleanField(blank = True,default=False)
    bio = models.TextField(blank = True)
    rating = models.DecimalField(decimal_places=1,max_digits=2,blank = True,null = True)


class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reviews = models.TextField()

