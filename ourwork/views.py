from django.shortcuts import render,redirect
from . models import headbanner,Work,ourwork_cat
import random
# Create your views here
def work(request ,num1= 0):
    if type(num1)==str:
        num1 = num1.replace('__','/')
        try:
            num1 =  ourwork_cat.objects.get(title = num1.replace('_',' ')).id
        except Exception as a:
            return redirect('home')
    color = ['casecolor1','bgsoiltracker ','bgdealer ','bgorbit ','hireux','jaccbg ','hawnk ','tayaar ','wepass ']
    Banner = headbanner.objects.filter(catagory= num1)
    WOrk = Work.objects.filter(catagory= num1)
    rep = []
    for i in WOrk:
        rep.append([i,random.choice(color)])
    res = {
        'title':ourwork_cat.objects.get(id=num1).title,
        'banner':Banner,
        'color': random.choice(color),
        'work':rep,
    }
    return render(request,'ourwork/base.html',res)
    return render(request,'ourwork/base.html',res)
