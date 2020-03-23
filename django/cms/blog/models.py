from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    statuses = [
        ('D','Draft'),
        ('P','Published'),
    ]
    title = models.CharField(max_length=256)
    content = models.TextField()
    status = models.CharField(max_length=1,choices=statuses)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts")
    images = models.ImageField(upload_to="blog/post",blank=True)

    def __str__(self):
        return self.title