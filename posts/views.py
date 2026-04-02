from django.shortcuts import render, redirect

from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone


def index(request):

    query = request.GET.get("search")

    posts = Post.objects.filter(created_at__lte=timezone.now()).order_by("-created_at")

    if query:
        posts = posts.filter(title__icontains=query)

    return render(request, "index.html", {"posts": posts})


def post_detail(request, pk):

    posts_detail = Post.objects.get(id=pk)

    return render(request, "post.html", {"posts_detail": posts_detail})


def create(request):

    if request.method == "POST":

        if not request.user.is_authenticated:
            request.session["draft_post"] = {
                "title": request.POST.get("title"),
                "body": request.POST.get("body"),
            }
            return redirect("/accounts/login/?next=/create")

        title = request.POST.get("title")
        body = request.POST.get("body")

        Post.objects.create(
            title=title,
            body=body,
        )

        request.session.pop("draft_post", None)
        return redirect("index")

    draft = request.session.get("draft_post", {})

    return render(
        request,
        "create.html",
        {"title": draft.get("title", ""), "body": draft.get("body", "")},
    )


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(request.GET.get("next", "/"))
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})
