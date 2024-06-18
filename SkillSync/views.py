from django.shortcuts import render
from projects.models import Project
from Blogs.models import Post

def projects(request):
    category = request.GET.get('category')
    if category:
        data = Project.objects.filter(category=category).order_by('-average_rating')
    else:
        data = Project.objects.all().order_by('-average_rating')
    return render(request, 'projects.html', {'data' : data})

def home(request):
    data = Post.objects.all()
    return render(request, 'home.html', {'data' : data})

def category_list(request):
    categories = Project.CATEGORY_CHOICES
    return render(request, 'category_list.html', {'categories': categories})


def blogs(request):
    data = Post.objects.all()
    return render(request, 'blogs.html', {'data' : data})