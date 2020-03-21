from django.shortcuts import render
from items.models import Categories
from django.http import HttpResponse

# Create your views here.


def index(request):
    items = Categories.objects.all()
    return render(request,'index.html',context={'items':items})


def products(request,category):
    category = Categories.objects.get(cat_name = category)
    products = category.products.all()
    return render(request,'products.html',context={'products':products})
