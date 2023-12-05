from django.shortcuts import render
from .models import Home


def home_page(request):
    return render(request, 'mytorrent/home.html')


def show_menu(request):
    info = Home.objects.all()
    return render(request, 'mytorrent/show_menu.html', {'info': info})
