from django.contrib import admin
from .models import Project, Skill, About, Experience, Certification, JourneyChapter

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed_date', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'completed_date')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'short_description', 'description')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Links', {
            'fields': ('project_url', 'github_url')
        }),
        ('Details', {
            'fields': ('technology_used', 'completed_date', 'is_featured')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)
    ordering = ('category', '-proficiency')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'location')
        }),
        ('Profile', {
            'fields': ('profile_image', 'bio', 'resume')
        }),
        ('Headings (English)', {
            'fields': ('heading_1', 'heading_2', 'heading_em', 'heading_3', 'education_text', 'cta_text')
        }),
        ('Headings (French)', {
            'fields': ('fr_heading_1', 'fr_heading_2', 'fr_heading_em', 'fr_heading_3', 'fr_education_text', 'fr_cta_text'),
            'classes': ('collapse',)
        }),
        ('Content (JSON)', {
            'fields': ('marquee_1', 'marquee_2', 'metrics'),
            'classes': ('collapse',)
        }),
    )

    def has_add_permission(self, request):
        """Only allow one About object"""
        return not About.objects.exists()

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'company', 'period', 'type', 'order')
    list_filter = ('type', 'fg', 'logo_placement')
    search_fields = ('company', 'role', 'location', 'summary')
    ordering = ('order', '-created_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('company', 'role', 'type', 'location', 'period', 'order')
        }),
        ('Content', {
            'fields': ('summary', 'achievements', 'outcome', 'skills')
        }),
        ('Styling & Logo', {
            'fields': ('color', 'fg', 'logo_image', 'logo_variant', 'logo_aspect', 'logo_placement')
        }),
        ('French Translation', {
            'fields': ('fr_role', 'fr_summary', 'fr_outcome', 'fr_achievements')
        }),
    )

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ('no', 'title', 'issuer', 'year', 'verified', 'order')
    list_filter = ('verified', 'issuer')
    search_fields = ('title', 'issuer', 'credential_id')
    ordering = ('order', '-created_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('no', 'title', 'issuer', 'year', 'order')
        }),
        ('Credential Status', {
            'fields': ('verified', 'credential_id', 'credential_url')
        }),
        ('Details', {
            'fields': ('skills', 'metric_value', 'metric_label')
        }),
        ('Logo', {
            'fields': ('logo_image', 'logo_aspect')
        }),
        ('French Translation', {
            'fields': ('fr_title', 'fr_skills', 'fr_metric_label')
        }),
    )

@admin.register(JourneyChapter)
class JourneyChapterAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'place', 'order')
    search_fields = ('year', 'title', 'place', 'story')
    ordering = ('order', '-created_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('year', 'title', 'place', 'order')
        }),
        ('Content', {
            'fields': ('story', 'bridge')
        }),
        ('French Translation', {
            'fields': ('fr_title', 'fr_place', 'fr_story', 'fr_bridge')
        }),
    )
