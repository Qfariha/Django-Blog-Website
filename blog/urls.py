from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='blog-home'), #empty path, home function created in views
    path('about/', views.about,name='blog-about'),
]