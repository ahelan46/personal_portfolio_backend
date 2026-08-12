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

class Experience(models.Model):
    """Model to store working experience"""
    TYPE_CHOICES = [
        ('Internship', 'Internship'),
        ('Full-time', 'Full-time'),
        ('Hackathon', 'Hackathon'),
        ('Freelance', 'Freelance'),
    ]
    
    FG_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    VARIANT_CHOICES = [
        ('tile', 'Tile'),
        ('plate', 'Plate'),
    ]

    PLACEMENT_CHOICES = [
        ('right', 'Right'),
        ('below', 'Below'),
    ]

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    location = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    summary = models.TextField()
    achievements = models.JSONField(default=list, help_text="List of achievements (strings)")
    outcome = models.CharField(max_length=300)
    skills = models.JSONField(default=list, help_text="List of skills (strings)")
    color = models.CharField(max_length=20, help_text="Hex color code (e.g. #0072E3)")
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
    
    # Frontend specific fields
    heading_1 = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. Design is how I think —")
    heading_2 = models.CharField(max_length=200, blank=True, null=True, help_text="e.g. business is how I")
    heading_em = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. aim")
    heading_3 = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. it.")
    education_text = models.CharField(max_length=500, blank=True, null=True, help_text="e.g. MSc International Business...")
    cta_text = models.CharField(max_length=100, blank=True, null=True, help_text="e.g. Explore My Work")
    
    fr_heading_1 = models.CharField(max_length=200, blank=True, null=True)
    fr_heading_2 = models.CharField(max_length=200, blank=True, null=True)
    fr_heading_em = models.CharField(max_length=100, blank=True, null=True)
    fr_heading_3 = models.CharField(max_length=100, blank=True, null=True)
    fr_education_text = models.CharField(max_length=500, blank=True, null=True)
    fr_cta_text = models.CharField(max_length=100, blank=True, null=True)
    
    marquee_1 = models.JSONField(default=list, blank=True, help_text="List of strings for top marquee")
    marquee_2 = models.JSONField(default=list, blank=True, help_text="List of strings for bottom marquee")
    metrics = models.JSONField(default=list, blank=True, help_text="List of metric objects")
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.name

class Experience(models.Model):
    """Model to store working experience"""
    TYPE_CHOICES = [
        ('Internship', 'Internship'),
        ('Full-time', 'Full-time'),
        ('Hackathon', 'Hackathon'),
        ('Freelance', 'Freelance'),
    ]
    
    FG_CHOICES = [
        ('light', 'Light'),
        ('dark', 'Dark'),
    ]

    VARIANT_CHOICES = [
        ('tile', 'Tile'),
        ('plate', 'Plate'),
    ]

    PLACEMENT_CHOICES = [
        ('right', 'Right'),
        ('below', 'Below'),
    ]

    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    location = models.CharField(max_length=200)
    period = models.CharField(max_length=100)
    summary = models.TextField()
    achievements = models.JSONField(default=list, help_text="List of achievements (strings)")
    outcome = models.CharField(max_length=300)
    skills = models.JSONField(default=list, help_text="List of skills (strings)")
    color = models.CharField(max_length=20, help_text="Hex color code (e.g. #0072E3)")
    fg = models.CharField(max_length=20, choices=FG_CHOICES, default='light')
    
    logo_image = models.ImageField(upload_to='portfolio/companies/', null=True, blank=True)
    logo_variant = models.CharField(max_length=20, choices=VARIANT_CHOICES, null=True, blank=True)
    logo_aspect = models.FloatField(null=True, blank=True, help_text="Aspect ratio (width / height)")
    logo_placement = models.CharField(max_length=20, choices=PLACEMENT_CHOICES, null=True, blank=True)
    
    fr_role = models.CharField(max_length=200, null=True, blank=True)
    fr_summary = models.TextField(null=True, blank=True)
    fr_outcome = models.CharField(max_length=300, null=True, blank=True)
    fr_achievements = models.JSONField(default=list, blank=True, help_text="French list of achievements (strings)")
    
    order = models.IntegerField(default=0, help_text="Order in which to display (lower is earlier)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.role} at {self.company}"

class Certification(models.Model):
    """Model to store professional certifications/credentials"""
    no = models.CharField(max_length=20, help_text="e.g. 2.1")
    issuer = models.CharField(max_length=200, null=True, blank=True)
    title = models.CharField(max_length=300)
    year = models.CharField(max_length=50, null=True, blank=True)
    credential_id = models.CharField(max_length=200, null=True, blank=True)
    credential_url = models.URLField(null=True, blank=True)
    verified = models.BooleanField(default=False)
    skills = models.JSONField(default=list, help_text="List of skills (strings)")
    metric_value = models.CharField(max_length=100, null=True, blank=True)
    metric_label = models.CharField(max_length=200, null=True, blank=True)
    
    logo_image = models.ImageField(upload_to='portfolio/issuers/', null=True, blank=True)
    logo_aspect = models.FloatField(null=True, blank=True, help_text="Aspect ratio (width / height)")
    
    fr_title = models.CharField(max_length=300, null=True, blank=True)
    fr_skills = models.JSONField(default=list, blank=True, help_text="French list of skills (strings)")
    fr_metric_label = models.CharField(max_length=200, null=True, blank=True)
    
    order = models.IntegerField(default=0, help_text="Order in which to display (lower is earlier)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title

class JourneyChapter(models.Model):
    """Model to store chapters for the Journey section"""
    year = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    story = models.TextField()
    bridge = models.TextField()
    
    fr_title = models.CharField(max_length=200, null=True, blank=True)
    fr_place = models.CharField(max_length=200, null=True, blank=True)
    fr_story = models.TextField(null=True, blank=True)
    fr_bridge = models.TextField(null=True, blank=True)
    
    order = models.IntegerField(default=0, help_text="Order in which to display (lower is earlier)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return f"{self.year} - {self.title}"
