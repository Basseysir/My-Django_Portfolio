from django.contrib import admin
from .models import Project, BlogPost, ContactMessage  # Ensure the dot '.' is there!

# Register your models here.
# portfolio/admin.py

admin.site.register(Project)
admin.site.register(ContactMessage)
admin.site.register(BlogPost)
