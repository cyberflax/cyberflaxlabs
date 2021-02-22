from django.shortcuts import render
from .models import project
from service.models import service,ServiceSubMenu


def index(request):
    Service = service.objects.all()
    Project = project.objects.all()
    responce = {
        'title':'HOME PAGE',
        'home':'active',
        'service': Service,
        'projects':Project
    }
    return render(request , 'index.html',responce)

def about(request):
    # qry = 'inspiron'
    # ob = service.objects.values('id','content')
    # for i in ob:
    #     if qry in i['content'].lower():
    #         a= i['content'].lower().replace(qry, 'Cyberflax')
    #         sub =  service.objects.get(id = i['id'])
    #         sub.content= a
    #         sub.save()
    #     else:
    #         print("false")
    a= search()
    responce = {
        'title':'ABOUT PAGE',
        'about':'active',
        
    }
    return render(request , 'about.html',responce)
def search():
    # qry = 'inspiron'
    # s= []
    # for item in s:
    #     ob = item._meta.get_fields()
    #     for i in ob :
    #         c=i
    #         i = str(i)
    #         if '<' in i:
    #             continue
    #         res  = i.rfind('.')
    #         if res != -1:
    #             i = (i[res+1:])
    #         ser = item.objects.values(i,"id")
    #         for a in ser:
    #             b= str(a[i])
    #             if qry in b.lower():
    #                 b= b.lower().replace(qry, 'Cyberflax')
    #                 print('true',i)
    #             else:
    #                 pass
    return 'res'