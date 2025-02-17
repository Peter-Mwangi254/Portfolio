from django.contrib import admin

from .models import Project, Skill, Blog, Contact

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "link", "github_link"]
    list_display_links = ["id", "title", "link", "github_link"]

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['id']

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'written_on', 'edited_on']
    list_display_links = ['id', 'title']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'submitted_on']
    list_display_links = ['name', 'subject', 'email']
    