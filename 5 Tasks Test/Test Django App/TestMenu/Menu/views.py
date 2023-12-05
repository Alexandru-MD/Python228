from django.shortcuts import render
from .models import MenuItem


def base(request):
    root_items = MenuItem.objects.all()
    return render(request, 'Menu/base.html', {'root_items': root_items})
