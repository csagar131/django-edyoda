from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from blog.forms import ContactForm
# Create your views here.


def index(request,*args,**kwargs):
    posts = Post.objects.all()
    return render(request,'blog/index.html',context={'posts':posts})


def blog_details(request,id,*args,**kwargs):
    post_details = Post.objects.get(id=id)
    return render(request,'blog/details.html',context={'post':post_details})

def contact_view(request,*args,**kwargs):

    if request.method == "GET":
        form = ContactForm()
        return render(request,'blog/contact.html',context={'form':form})
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponse("Thank you")
        else:
            return render(request,'blog/contact.html',context={'form':form})


    
