from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.all()
    #print(post)
    data={
        "posts":posts
    }
    return render(request,"home.html",data)


def post(request,url):
    post=Post.objects.get(url=url)
    #print(post)
    return render(request,"post.html",{'post':post})
