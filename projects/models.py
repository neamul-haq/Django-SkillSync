from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('Django', 'Django'),
        ('Android', 'Android'),
        ('PHP', 'PHP'),
        ('Spring', 'Spring'),
        ('Nodejs', 'Nodejs'),
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    screenshots = models.ImageField(upload_to='projects/media/uploads/')
    technologies = models.CharField(max_length=100)
    live_site_link = models.URLField(max_length=200, null=True, blank=True)
    RatePeopleNo = models.IntegerField(default=0)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)
    lastRating = models.PositiveIntegerField(default=0, choices=[(i,i) for i in range(0, 8)])
    
    def __str__(self):
        return self.title 