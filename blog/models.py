from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#classes are tables in db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    #User table is the Foreign Key of post table and if the user is deleted, posts are deleted

    def __str__(self):
        return self.title