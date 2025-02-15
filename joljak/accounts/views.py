from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('mock_investment:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'fomr':form})

def logout_view(request):
    logout(request)
    return redirect('accoounts:login')