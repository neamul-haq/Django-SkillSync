from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from . import forms
from . import models
from django.contrib import messages
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AddProjectCreateView(CreateView):
    model = models.Project
    form_class = forms.ProjectForm
    template_name = 'add_project.html'
    success_url = reverse_lazy('projects')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

    
def AddRating(request, project_id):
    project = models.Project.objects.get(id=project_id)
    if request.method == 'POST':
        rating_form = forms.RatingForm(request.POST, instance=project)
        if rating_form.is_valid():
            rating_form.save() 
            project.average_rating = (project.average_rating*project.RatePeopleNo + project.lastRating) / (project.RatePeopleNo+1)
            project.RatePeopleNo +=1
            rating_form = forms.RatingForm(request.POST, instance=project)
            rating_form.save() 
            messages.success(request, 'Rating added successfully!')
            return redirect('projects')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        rating_form = forms.RatingForm(instance=project)
    return render(request, 'rating.html', {'form': rating_form})


class DetailProjectView(DetailView):
    model = models.Project
    pk_url_kwarg = 'id'
    template_name = 'project_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
