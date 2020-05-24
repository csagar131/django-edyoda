from django.db import models
from accounts.models import User


class CareRequests(models.Model):

    statuses = [
        ('approved','a'),('rejected','r'),('pending','p'),('completed','c'),('active','A'),
    ]

    caregiver = models.ForeignKey(User,models.CASCADE,related_name = 'givers')
    careseeker = models.ForeignKey(User,models.CASCADE,related_name = 'seekers')
    status = models.CharField(max_length = 50,choices = statuses)

    def __str__(self):
        return "{}-{}".format(self.caregiver.username,self.careseeker.username)

    def get_request_status(self):
        return self.status