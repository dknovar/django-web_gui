from django.shortcuts import render
from django.http import HttpResponse
from. models import info 
# Create your views here.

def index(request):
    #query
    infos = info.objects.all()

    contex = {
        'judul':'About Opang',
        'penulis':'Iya Opang',
        'banner':'img/a.jpg',
        'infos': infos,
    }
    return render(request,'about/index.html',contex)

def recents(request):
    return render(request, 'about/test_pusher.html')