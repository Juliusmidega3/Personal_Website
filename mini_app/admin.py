from django.contrib import admin
from .models import Skill, Service, Project, Counter, PortfolioItem

# Register the Skill model
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'level')
    search_fields = ('name',)

# Register the Service model
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

# Register the Project model
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    search_fields = ('title',)

# Register the Counter model
@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('title', 'value')
    search_fields = ('title',)

# Register the PortfolioItem model
@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'link')
    search_fields = ('title',)

# Register your models here.
