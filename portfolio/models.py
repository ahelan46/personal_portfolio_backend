from django.db import models
from django.utils import timezone


class Project(models.Model):
    """Model to store portfolio projects"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='portfolio/projects/', null=True, blank=True)
    technology_used = models.CharField(max_length=500, help_text="Comma-separated technologies")
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    completed_date = models.DateField(default=timezone.now)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-completed_date']

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Model to store technical skills"""
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools & Others'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    proficiency = models.IntegerField(help_text="Rate from 1-100", default=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', '-proficiency']

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"


class About(models.Model):
    """Model to store about section"""
    name = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    resume = models.FileField(upload_to='portfolio/', null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.name
