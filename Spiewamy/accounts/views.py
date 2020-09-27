from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def login_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse('Zły login i haslo')

def register_view(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = ''
        if password == password2:
            user = User.objects.create_user(username, email, password)
            return redirect('/')
        else:
            return HttpResponse('podaj poprawne hasło')




def logout_view(request):
    logout(request)
    return redirect('/')