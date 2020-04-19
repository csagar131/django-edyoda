from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category
from blog.forms import ContactForm,PostForm,Search
from django.views.generic import ListView,DetailView,FormView,CreateView,UpdateView
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin


class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = 'posts'
    queryset = Post.objects.filter(status = "P")
 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
        

class CategoryIndexView(ListView):
    model = Post
    template_name = 'blog/category_index.html'
    context_object_name = 'category'
    queryset = Category.objects.all()

    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        categoryobj = Category.objects.get(slug = self.kwargs['slug'])
        posts = Post.objects.filter(category = categoryobj)
        context['posts'] = posts
        return context


class BlogDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login'
    model = Post
    template_name = 'blog/details.html'
    context_object_name = 'post'
 

class ContactFormView(FormView):
    form_class = ContactForm
    success_url = 'contact'
    template_name = 'blog/contact.html'

    def form_valid(self,form):
        print(form.cleaned_data)
        return super().form_valid(form)


class PostModelFormView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url = 'login'
    permission_required = 'blog.add_post'
    template_name =  'blog/post.html'
    form_class = PostForm


class PostFormUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url ='login'
    permission_required = 'blog.change_post'
    model = Post
    form_class = PostForm
    template_name = 'blog/post.html'





