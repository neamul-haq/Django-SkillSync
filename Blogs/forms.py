from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta: 
        model = Post
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 6, 'cols': 80}),
        }
        
class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']

