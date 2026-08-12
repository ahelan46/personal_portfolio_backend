from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Project, Skill, About
from django.db import OperationalError
from django.http import FileResponse, HttpResponse
from django.conf import settings
import os


def home(request):
    """Serve React frontend (SPA) from built Vite app"""
    # Try to serve the built React index.html directly
    react_index_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'dist', 'index.html')
    
    try:
        if os.path.exists(react_index_path):
            with open(react_index_path, 'r', encoding='utf-8') as f:
                return HttpResponse(f.read(), content_type='text/html')
    except Exception as e:
        print(f"Error loading React index: {e}")
    
    # Fallback if React app not built
    return HttpResponse("<h1>Portfolio App Loading...</h1><p>React app is not built yet. Please run: npm run build</p>")


class ProjectListView(ListView):
    """Display all projects"""
    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'
    paginate_by = 6


class ProjectDetailView(DetailView):
    """Display project details"""
    model = Project
    template_name = 'portfolio/project_detail.html'
    context_object_name = 'project'
    slug_field = 'title'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        """Allow getting by pk or title"""
        obj = super().get_object(queryset)
        return obj


def about_view(request):
    """About page view"""
    about = About.objects.first()
    skills = Skill.objects.all()
    
    context = {
        'about': about,
        'skills': skills,
    }
    return render(request, 'portfolio/about.html', context)


def skills_view(request):
    """Skills page view"""
    skills = Skill.objects.all()
    categories = {}
    
    for skill in skills:
        category = skill.get_category_display()
        if category not in categories:
            categories[category] = []
        categories[category].append(skill)
    
    context = {
        'skills': skills,
        'categories': categories,
    }
    return render(request, 'portfolio/skills.html', context)


def contact_view(request):
    """Contact page view"""
    about = About.objects.first()
    context = {'about': about}
    return render(request, 'portfolio/contact.html', context)


def contact(request):
    about = About.objects.first()
    
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # (You can save or email the message here)

        messages.success(request, "Your message has been sent successfully!")
        return redirect("portfolio:contact")

    context = {'about': about}
    return render(request, "portfolio/contact.html", context)