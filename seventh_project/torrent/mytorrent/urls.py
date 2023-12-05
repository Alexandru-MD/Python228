from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='index'),
    path('show-menu/', views.show_menu, name='show-menu')
]