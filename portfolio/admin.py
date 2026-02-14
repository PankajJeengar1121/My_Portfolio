# portfolio/admin.py
from django.contrib import admin
from .models import Project, Skill, ContactMessage

# Option 1: Basic Registration (Simplest)
# admin.site.register(Project)
# admin.site.register(Skill)
# admin.site.register(ContactMessage)

# Option 2: Custom Registration (Better UI)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon_class')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    readonly_fields = ('name', 'email', 'message', 'sent_at') # Prevent editing messages