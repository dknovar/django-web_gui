from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    contex = {
        # 'judul':'About Opang',
        # 'penulis':'Iya Opang',
        # 'banner':'img/a.jpg',
    }
    return render(request,'login/index.html',contex)

def recents(request):
    return HttpResponse('INI ADALAH RECENTS')

def daftar(request):
    return render(request,'login/daftar.html')

def lupapass(request):
    return render(request,'login/lupapass.html')