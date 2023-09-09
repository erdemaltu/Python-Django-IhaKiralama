from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from ihalar.models import Kiralama, Iha
from hesaplar.models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect

#NOT:Veri ile alakalı işlemlerin hepsi html sayfalarında jquary ile yapılmıştır, sadece örnek olması açısından kiralamaların olduğu sayfada sadece kiralanlar listesi ve kullanıcı çıkış işlemi view üzerinden yapılmıştır

def index(request):#anasayfa view'i
    
    return render(request, 'index.html')#html sayfa görüntülemesi

@login_required(login_url='/login')
def iha_list(request):#ihalar view'i
    
    return render(request, 'ihalar.html')

@login_required(login_url='/login')
def kiralama_list(request):#kiralamalar view'i

    kiralama = Kiralama.objects.all().order_by('-created_at')
    uyeler = CustomUser.objects.all()
    ihalar = Iha.objects.all()
    context = {
        'kiralama':kiralama,
        'uyeler':uyeler,
        'ihalar':ihalar,
    }
    return render(request, 'kiralama.html', context)

def user_login(request):#kullanıcı giriş view'i
    form = LoginForm()

    return render (request, 'login.html', {'form':form})


def user_register(request):#kullanıcı kayıt view'i
    form = RegisterForm()

    return render(request, 'register.html', {'form':form})

def user_logout(request):#kullanıcı çıkış view'i
    logout(request)
    return redirect('index')
