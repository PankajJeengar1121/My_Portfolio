# portfolio/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill
from .forms import ContactForm

def index(request):
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'portfolio/index.html', {
        'projects': projects,
        'skills': skills,
        'form': form
    })