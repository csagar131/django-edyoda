from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="users") 
    quantity = models.IntegerField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="products")


