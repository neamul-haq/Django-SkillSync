from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta: 
        model = Project
        exclude = ['author', 'RatePeopleNo', 'average_rating', 'lastRating']
        
        
class RatingForm(forms.ModelForm):
    class Meta: 
        model = Project
        fields = ['lastRating',]