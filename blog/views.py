from django.shortcuts import render
from .models import Post


def home(request): #Handling when a user goes to blog homepage
  context={
    'posts':Post.objects.all() # Post is the class in model.py, fetching from db
  }
  return render(request, 'blog/home.html', context) 
    # rendering the home.html from blog directory
    # render returning HTTPresponse
     

def about(request):
  return render(request, 'blog/about.html',{'title': 'About'})