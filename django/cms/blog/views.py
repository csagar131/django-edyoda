from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category
from blog.forms import ContactForm,PostForm,Search
# Create your views here.


def index(request,*args,**kwargs):
    posts = Post.objects.all()
    category = Category.objects.all()
    if request.method == "GET":
        form = Search()
        return render(request,'blog/index.html',context={'posts':posts,'category':category,'form':form})
    else:
        form = Search(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('search_blog')
            print(text)
            posts = Post.objects.filter(title__contains = text)
            return render(request,'blog/index.html',context={'posts':posts,'category':category,'form':form})
        return render(request,'blog/index.html',context={'posts':posts,'category':category,'form':form})



def category_index(request,id,*args,**kwargs):
    catall = Category.objects.all()
    category = Category.objects.get(id = id)
    posts = Post.objects.filter(category = category)
    print(posts)
    return render(request,'blog/category_index.html',context={'posts':posts,'category':catall})

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


    
def post_model_form(request,*args,**kwargs):
    if request.method == "GET":
        form = PostForm()
        return render(request,'blog/post.html',context={'form':form})

    else:
        print(request.POST)
        print(request.FILES)
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('images')
            # print(image.__dict__)
            form.save()
            return HttpResponse("Thanking You")
        return render(request,'blog/post.html',context={'form':form})


def post_edit_model_form(request,id,*args,**kwargs):
    try:
        post = Post.objects.get(id = id)
    except:
        return HttpResponse("Invalid id")

    if request.method == "GET":
        form = PostForm(instance = post)
        return render(request,'blog/post.html',context={'form':form})

    form = PostForm(request.POST,request.FILES,instance = post)
    if form.is_valid():
        form.save()
        return render(request,'blog/post.html',context={'form':form})
    return render(request,'blog/post.html',context={'form':form})


