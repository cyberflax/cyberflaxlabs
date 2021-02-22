from django.contrib import admin
from . models import blog,catagory,News
# Register your models here.
admin.site.register(catagory)
admin.site.register(blog)
admin.site.register(News)