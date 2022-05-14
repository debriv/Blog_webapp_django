from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile.pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args,**kwargs)

        img= Image.open(self.image.path)


        if img.size[0] > 300 or img.size[1] >300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
# Create your models here.
