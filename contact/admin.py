from django.contrib import admin
from . models import OurContact,contactReq
# Register your models here.

class contactReqAdmin(admin.ModelAdmin):
    list_display = ('name','email','intrest','Phone')
admin.site.register(OurContact)
admin.site.register(contactReq,contactReqAdmin)