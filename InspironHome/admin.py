from django.contrib import admin

# Register your models here.
from .models import project,ourwork,homebanner

admin.site.register(project)
admin.site.register(ourwork)
admin.site.register(homebanner)
