from django.db import models

# Create your models here.

class Categories(models.Model):
    cat_image =  models.ImageField(upload_to="categories/images")
    cat_name = models.CharField(max_length=50)
    cat_description = models.TextField()

    def __str__(self):
        return self.cat_name


class Products(models.Model):
    p_image = models.ImageField(upload_to="products/images")
    p_name = models.CharField(max_length=50)
    p_price = models.IntegerField()
    p_category = models.ForeignKey(Categories,on_delete=models.CASCADE,related_name="products")
    p_description = models.TextField(default=None)

    def __str__(self):
        return self.p_name



