from django.db import models
import datetime
# Create your models here.
class catagory(models.Model):
    catagory = models.CharField(max_length=50)
    def __str__(self):
        return self.catagory
class  blog(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_content = models.CharField(max_length=5000)
	blog_time = models.DateTimeField(auto_now=True)
	blog_share = models.IntegerField(default=0)
	blog_views = models.IntegerField(default=0)
	blog_owner = models.CharField(max_length=50)
	blog_image = models.ImageField(upload_to = 'wesiteblog/images', default= "")
	blog_catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
	def __str__(self):
		return self.blog_owner
class  News(models.Model):
	blog_title = models.CharField(max_length=50)
	blog_content = models.CharField(max_length=5000)
	blog_time = models.DateTimeField(auto_now=True)
	blog_share = models.IntegerField(default=0)
	blog_views = models.IntegerField(default=0)
	blog_owners = models.CharField(max_length=50)
	blog_image = models.ImageField(upload_to = 'wesiteblog/images', default= "")
	blog_catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
	def __str__(self):
		return self.blog_owners