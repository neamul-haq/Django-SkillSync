from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

    
@login_required
def add_post(request):
    data = models.Post.objects.filter(author = request.user)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, request.FILES) 
        if post_form.is_valid(): 
            post_form.instance.author = request.user
            post_form.save() 
    else:
        post_form = forms.PostForm()
    return render(request, 'add_post.html', {'form' : post_form, 'data':data})
    

@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('add_post')
    

@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = models.Post
    template_name = 'delete.html'
    success_url = reverse_lazy('add_post')
    pk_url_kwarg = 'id'


class DetailPostView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    
    

