from django.shortcuts import render
from . models import blog,catagory,News
# Create your views here.
def Blog(request,num=0):
    if num == 0:
        Blogs= blog.objects.all()
        responce={
            'title':'BLOGS',
            'blog': 'active',
            'blogs':Blogs
        }
        return render(request,'blog/blog.html',responce)
    Blogs= blog.objects.get(id= num)
    Blogss= blog.objects.all()[:3]
    responce= {
        'title': Blogs.blog_title,
        'bl':'active',
       'blog':Blogs ,
       'blogs':Blogss 
    }
    return render(request,'blog/post.html',responce)
def news(request, num=0):
    if num == 0:
        NEWS = News.objects.all()

        responce={
            'title':'News',
            'news': 'active',
            'blogs':NEWS
        }
        return render(request,'blog/news1.html',responce)
    Blogs= News.objects.get(id= num)
    Blogss= blog.objects.all()[:3]
    responce= {
        'title': Blogs.blog_title,
       'blog':Blogs ,
       'ne': 'active',
       'blogs':Blogss 
    }
    return render(request,'blog/post.html',responce)
    