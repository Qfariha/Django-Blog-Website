from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


#classes are tables in db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    #User table is the Foreign Key of post table and if the user is deleted, posts are deleted

    def __str__(self): #a special method that defines how an object is represented as a string.
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk}) #full path as string