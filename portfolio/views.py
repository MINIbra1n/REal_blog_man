from django.shortcuts import render
from .models import Project # Импорт всех моделей из класса Project из фаила models.py в папки portfolio 

def home(request):
    projects= Project.objects.all()
    return render(request, 'portfolio/home.html',{'projects':projects})


def all_blogs(request):
    return render(request, 'blog/all_blogs.html',{'all_blogs':all_blogs})