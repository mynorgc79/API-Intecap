from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Usuario
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.hashers import make_password

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            return redirect('task:inicio')  # Redirige al index.html después de la autenticación exitosa
    return render(request, 'login.html')


def inicio(request):
    return render(request, 'index.html')