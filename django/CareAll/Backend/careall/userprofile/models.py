from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
    genders = [
        ("M","MALE"),("F","FEMALE"),
    ]

    email = models.EmailField()
    age = models.IntegerField(blank = True)
    gender = models.CharField(max_length=1,choices = genders,default = 'M')
    address = models.CharField(max_length=255,blank = True)
    Phone = models.IntegerField()
    is_elder = models.BooleanField(blank = True)


    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name


