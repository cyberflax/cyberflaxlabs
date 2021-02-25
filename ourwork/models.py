from django.db import models

# Create your models here.
class ourwork_cat(models.Model):
    title = models.CharField(max_length= 100)
    def __str__(self):
        return self.title
class headbanner (models.Model):
    catagory = models.ForeignKey(ourwork_cat, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length= 100)
    content = models.CharField(max_length= 5000)
    projecticon = models.ImageField(upload_to="ourwork/projecticon")
    projectimage = models.ImageField(upload_to="ourwork/projectimage")
    projectTitle = models.CharField(max_length= 200)
    projectsource = models.ImageField(upload_to="ourwork/projectsource")
    sourceLink= models.CharField(max_length= 500)
    projectlink= models.CharField(max_length= 500,blank = True)
    def __str__(self):
        return str(self.catagory)

class Work(models.Model):
    catagory = models.ForeignKey(ourwork_cat, on_delete=models.CASCADE,default=1)
    projectimage = models.FileField(upload_to="ourwork/projectimage" , blank = True)
    projecticon = models.FileField(upload_to="ourwork/projecticon",blank = True)
    projectTitle = models.CharField(max_length= 200,blank = True)
    content = models.CharField(max_length= 5000,blank = True)
    projectsource = models.FileField(upload_to="ourwork/projectsource",blank = True)
    sourceLink= models.CharField(max_length= 500,blank = True)
    projectsource1 = models.FileField(upload_to="ourwork/projectsource",blank = True)
    sourceLink1= models.CharField(max_length= 500,blank = True)
    projectlink= models.CharField(max_length= 500,blank = True)
    def __str__(self):
        return str(self.catagory)