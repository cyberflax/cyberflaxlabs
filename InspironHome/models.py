from django.db import models

# Create your models here.
class project(models.Model):
    icon = models.ImageField(upload_to = 'project/ourwork',default= '')
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    def __str__(self):
        return self.title
class ourwork(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title