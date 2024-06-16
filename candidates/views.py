from django.shortcuts import render, redirect
from . import forms
from .models import Profile
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login , update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView


def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)
        user = request.user
        
        # Check if the profile exists, if not, create it
        # if not Profile.objects.filter(user=user).exists():
        #     Profile.objects.create(user=user)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()
    return render(request, 'register.html', {'form' : register_form, 'type' : 'Register'})



class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Logged in Successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Logged in information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
    



# @login_required
# def profile(request):
#     data = Post.objects.filter(author = request.user)
#     return render(request, 'profile.html', {'data' : data})


@login_required
def profile(request):
    user = request.user
    if not Profile.objects.filter(user=user).exists():
        Profile.objects.create(user=user)
    profile = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        user_form = forms.ChangeUserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')

    else:
        user_form = forms.ChangeUserForm(instance=user)
        profile_form = forms.ProfileForm(instance=profile)

    return render(request, 'update_profile.html', {'user_form': user_form, 'profile_form': profile_form,'profile':profile})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated Successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form})


def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required
def resume(request):
    user = request.user
    profile = Profile.objects.get(user = request.user)

    if request.method == 'POST':
        resume_form = forms.ResumeForm(request.POST, request.FILES, instance=profile)

        if resume_form.is_valid():
            resume_form.save()
            messages.success(request, 'Resume updated successfully')

    else:
        resume_form = forms.ResumeForm(instance=profile)

    return render(request, 'resume.html', {'resume_form': resume_form, 'profile':profile})