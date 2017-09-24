from django.contrib import admin
from .models import Project, Image

# Register your models here.

class ProjectImageInLine(admin.TabularInline):
    model = Image
    extra = 25

class ProjectAdmin(admin.ModelAdmin):
    inlines = [ ProjectImageInLine, ]

admin.site.register(Project, ProjectAdmin)
admin.site.register(Image)

