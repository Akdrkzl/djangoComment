from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UyeGiris(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            print(username)
            print(password)

            user = authenticate( username = username,password = password)

            if user is not None:
                login(request,user)
                next_url = request.GET.get('next', None)
                messages.success(request,'Giriş Başarılı')
                if next_url is None:
                    return redirect('index')
                else:
                    return redirect(next_url)
            else:
                messages.error(request,'Kullanici Adı veya Şifre Yanlış')
                return render(request,'login.html',{'form':form})
        else:
            messages.error(request,'Kullanici Adı veya Şifre Yanlış')
            return render(request,'login.html',{'form':form})
    form = UyeGiris()
    return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    messages.info(request,'Çıkış Yapıldı')
    return redirect('login')


def user_register(request):
    if request.method == 'POST':
        form = UyeKayitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    form = UyeKayitForm()
    return render(request,'register.html',{'form':form})

def sifre_degistir(request):
    if request.method == 'POST':
        form = SifreDegistir(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('index')
        else:
            return render(request,'sifredegistir.html',{'form':form})

    form = SifreDegistir(request.user)
    return render(request,'sifredegistir.html',{'form':form})