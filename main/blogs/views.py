from django.shortcuts import render
from .models import Blog
# Create your views here.


def blogs(request):
    content = {"blogs": Blog.objects.all()}
    return render(request, 'blogs.html', content)


def blog(request, pk):
    content = {"blog": Blog.objects.get(id=pk)}
    return render(request, 'blog.html', content)
