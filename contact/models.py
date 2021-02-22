from django.db import models

# Create your models here.
class OurContact(models.Model):
    projectEnq = models.CharField(max_length= 50)
    genralEnq = models.CharField(max_length= 50)
    carrerEnq = models.CharField(max_length= 50)
    patnershipEnq = models.CharField(max_length= 50)
    locationTitle = models.CharField(max_length= 50)
    location = models.CharField(max_length= 500)
    Enq = models.CharField(max_length= 50)
    def __str__(self):
        return self.projectEnq
class contactReq(models.Model):
    name =  models.CharField(max_length= 50)
    email =  models.CharField(max_length= 50)
    Phone =  models.CharField(max_length= 50)
    intrest =  models.CharField(max_length= 50)
    Message =  models.CharField(max_length= 5000)
    def __str__(self):
        return self.name