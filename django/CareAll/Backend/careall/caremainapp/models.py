from django.db import models
from userprofile.models import User
# Create your models here.


class Reviews(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="ureviews")
    reviews = models.TextField()
    review_by = models.OneToOneField(User,on_delete=models.CASCADE)

class Rating(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    rating = models.DecimalField(decimal_places=1,max_digits=2,blank = True,null = True)