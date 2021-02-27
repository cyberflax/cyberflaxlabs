from django.contrib import admin
from .models import ourwork_cat,headbanner,Work
# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ['catagory','projectTitle','content']
admin.site.register(ourwork_cat)
admin.site.register(headbanner)
