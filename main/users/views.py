from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.db.models import Q
from django.contrib import messages
from blogs.models import Blog
from .models import User, UserProfile


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            print("try entered")
            user = User.objects.get(username=username)
        except:
            print("catch entered")
            user = authenticate(request, username=username, password=password)

        if user is not None:
            print("user not none")
            login(request, user)
            return redirect(request, 'blogs')

    return render(request, 'login.html')


def logout_page(request):
    ...


def signup(request):
    ...


def account(request, pk):
    user = UserProfile.objects.get(id=pk)
    blogs = Blog.objects.filter(Q(owner__id=user.id))
    return render(request, 'user_blogs.html', {"blogs": blogs})
