from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import AuthenticationForm

def make_logout(request):
    logout(request)
    return redirect('people_list')

def make_login(request):
    login_form = AuthenticationForm()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('people_list')
    
    return render(request, "login.html", {'form': login_form})