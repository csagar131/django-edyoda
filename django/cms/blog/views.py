from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
# Create your views here.


def index(request,*args,**kwargs):
    posts = Post.objects.all()
    return render(request,'blog/index.html',context={'posts':posts})


def blog_details(request,id,*args,**kwargs):
    post_details = Post.objects.get(id=id)
    return render(request,'blog/details.html',context={'post':post_details})