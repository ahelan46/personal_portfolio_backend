from django.contrib import messages
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from .models import Project, Skill, About


def home(request):
    """Home page view"""
    featured_projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all()
    
    try:
        about = About.objects.first()
    except About.DoesNotExist:
        about = None
    
    context = {
        'featured_projects': featured_projects,
        'skills': skills,
        'about': about,
    }
    return render(request, 'portfolio/home.html', context)


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