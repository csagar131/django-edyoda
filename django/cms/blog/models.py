from django.db import models

# Create your models here.
class Post(models.Model):
    statuses = [
        ('D','Draft'),
        ('P','Published'),
    ]
    title = models.CharField(max_length=256)
    content = models.TextField()
    status = models.CharField(max_length=1,choices=statuses)

    def __str__(self):
        return self.title