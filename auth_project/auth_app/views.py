from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .middlewares import auth,guest
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.utils import timezone
# Create your views here.

@auth
def profile(request):
    current_time = timezone.now()
    return render(request, 'auth/profile.html', {'user': request.user,'current_time': current_time,})

@auth
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'auth/change_password.html', {'form': form})

@guest
def regis(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'','password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'auth/register.html',{'form':form})

@guest
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'', 'password':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'auth/login.html',{'form':form})

@auth
def dash_board(request):
  return render(request,'dashboard.html')

def log_out(request):
  logout(request)
  return redirect('login')