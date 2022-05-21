from django.contrib import admin

# Register your models here.

# First import from project folder
from .models import Project
# Then register each individual model with the admin.site.register()
admin.site.register(Project)