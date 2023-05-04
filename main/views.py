from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Post


@login_required(login_url="/login")
def home(request):
    posts = Post.objects.all()
    form = PostForm()

    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        post = Post.objects.filter(id=post_id).first()
        if post and post.author == request.user:
            post.delete()
        else:
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect("/home")

    return render(request, 'main/home.html', {'posts': posts, 'form': form})



@login_required(login_url="/login")
def meus_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'main/meus_posts.html', {"posts": posts})


def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign-up.html', {"form": form})
