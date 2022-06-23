from django.shortcuts import render

# Create your views here.
from .models import Category, Post

# create home view here

categories = Category.objects.all() 
posts = Post.objects.all()

def home(request):
    return render(request, "index.html", {'title': "Home Page", 'posts': posts[:6], 'categories': categories})

def post(request, url):
    post = Post.objects.get(url=url)
    return render(request, 'post.html',{'post':post, 'categories':categories})

def category(request, url):
    cat = Category.object.get(url=url)
    posts = Post.object.filter(cat=cat)
    return render(request, 'category.html',{"cat":cat, "posts":posts})
