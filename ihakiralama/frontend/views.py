from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from ihalar.models import Kiralama, Iha
from hesaplar.models import CustomUser
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
    
    return render(request, 'index.html')

@login_required(login_url='/login')
def iha_list(request):
    
    return render(request, 'ihalar.html')

@login_required(login_url='/login')
def kiralama_list(request):

    kiralama = Kiralama.objects.all().order_by('-created_at')
    uyeler = CustomUser.objects.all()
    ihalar = Iha.objects.all()
    context = {
        'kiralama':kiralama,
        'uyeler':uyeler,
        'ihalar':ihalar,
    }
    return render(request, 'kiralama.html', context)

def user_login(request):
    form = LoginForm()

    return render (request, 'login.html', {'form':form})


def user_register(request):
    form = RegisterForm()

    return render(request, 'register.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('index')
