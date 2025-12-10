from django.shortcuts import render,redirect

from .models import Post

def index(request):

    posts=Post.objects.all()

    return render(request,'index.html',{'posts':posts})


def post_detail(request,pk):

    posts_detail=Post.objects.get(id=pk)

    return render(request,'post.html',{'posts_detail':posts_detail})


def create(request):

    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('body')

        Post.objects.create(title=title, body=body)

        return redirect('index')

    return render(request,'create.html')
