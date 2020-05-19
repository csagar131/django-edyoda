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


class CareRequest(models.Model):
    request_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="req_by")
    request_to = models.ForeignKey(User,on_delete=models.CASCADE)
    req_status = models.BooleanField(blank = True)
    appr_status = models.BooleanField(blank = True)

    def __str__(self):
        return "{},{}".format(self.request_by.username,self.request_to.username)

    class Meta:
        unique_together = (('request_by', 'request_to'),)