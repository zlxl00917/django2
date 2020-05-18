from django.shortcuts import render, redirect
from .models import Post 
import datetime

# Create your views here.

def index(request):
    movies=Post.objects.filter(category='movie')
    movies_num=movies.count()
    dramas=Post.objects.filter(category='drama')
    dramas_num=dramas.count()
    entertainments=Post.objects.filter(category='entertainment')
    entertainments_num=entertainments.count()
    return render(request, 'index.html', {'movies_num':movies_num, 'dramas_num':dramas_num, 'entertainments_num':entertainments_num}) 


def movie(request):
    movie=Post.objects.filter(category='movie')
    return render(request, 'movie.html', {'movie':movie})

def drama(request):
    drama=Post.objects.filter(category='drama')
    return render(request, 'drama.html', {'drama':drama})

def entertainment(request):
    entertainment=Post.objects.filter(category='entertainment')
    return render(request, 'entertainment.html', {'entertainment': entertainment})

def detail(request,pk_of_clicked):
    post=Post.objects.get(pk=pk_of_clicked)
    return render(request, 'detail.html',{'post' : post})

def new(request):
    dt = datetime.datetime.now()
    nowDatetime=dt.strftime('%Y-%m-%d %H:%M:%S')
    if request.method == 'POST':
        print(request.POST)
        new_post=Post.objects.create(
            title=request.POST['title'],
            article=request.POST['article'],
            category=request.POST['category'],
            date=nowDatetime
        )
        return redirect('detail',pk_of_clicked=new_post.pk)
    else:
        return render(request,'new.html')



    

