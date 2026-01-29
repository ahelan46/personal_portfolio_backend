from django.contrib import admin
from .models import Project, Skill, About


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
            'fields': ('profile_image', 'bio')
        }),
        ('Files', {
            'fields': ('resume',)
        }),
    )

    def has_add_permission(self, request):
        """Only allow one About object"""
        return not About.objects.exists()
