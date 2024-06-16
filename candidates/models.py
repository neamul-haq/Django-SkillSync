from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='candidates/media/uploads/', null=True, blank=True)
    cv = models.FileField(upload_to='candidates/media/cvs/', null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'