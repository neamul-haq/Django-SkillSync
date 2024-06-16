from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    )
    name = models.CharField(max_length=100)
    proficiency_levels = models.CharField(max_length=50, choices=LEVEL_CHOICES)
    user = models.ManyToManyField(User)
    
    def __str__(self):
        return self.name
