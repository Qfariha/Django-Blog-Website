from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView, CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request): #Handling when a user goes to blog homepage
  context={
    'posts':Post.objects.all() # Post is the class in model.py, fetching from db
  }
  return render(request, 'blog/home.html', context) 
    # rendering the home.html from blog directory
    # render returning HTTPresponse

class PostListView(ListView):
  model=Post  
  template_name='blog/home.html'  # <app>/<model>_<viewtype>.html!
  context_object_name='posts'
  ordering=['-date_posted']

class PostDetailView(DetailView):
  model=Post  

class PostCreateView(LoginRequiredMixin,CreateView):
  model=Post  
  fields=['title','content']

  def form_valid(self,form):
    form.instance.author=self.request.user #Setting the author beforing creating new post
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  model=Post  
  fields=['title','content']

  def form_valid(self,form):
    form.instance.author=self.request.user #Setting the author beforing creating new post
    return super().form_valid(form)
  
  def test_func(self):
    post=self.get_object()
    if self.request.user == post.author:
      return True
    return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
  model=Post
  success_url='/' 
  def test_func(self):
    post=self.get_object()
    if self.request.user == post.author:
      return True
    return False

def about(request):
  return render(request, 'blog/about.html',{'title': 'About'})



