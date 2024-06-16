from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill
from .forms import SkillForm

@login_required
def skill_list(request):
    # Get the skills associated with the current user
    skills = Skill.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = SkillForm(request.POST)
        if form.is_valid():
            skill_name = form.cleaned_data['name']
            proficiency_level = form.cleaned_data['proficiency_levels']
            
            # Check if the skill already exists
            skill, created = Skill.objects.get_or_create(name=skill_name, proficiency_levels=proficiency_level)
            skill.user.add(request.user)
            skill.save()

            messages.success(request, 'Skill added successfully!')
            return redirect('skill_list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SkillForm()

    return render(request, 'skill_list.html', {'skills': skills, 'form': form})
