from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self): #A special method that defines how an object is represented as a string.
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):  # Accept additional arguments
        super().save(*args, **kwargs)  # Pass them to the parent save() method
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)








