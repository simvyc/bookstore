from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Account
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            # Create the account and auto-generate the username
            Account.objects.create_user(name=name, surname=surname, email=email, password=password)
            
            return redirect('login')  
    else:
        form = RegistrationForm()
    
    return render(request, 'accounts/register.html', {'form': form})



def login(request):
    if request.user.is_authenticated:
        # return redirect('profile')
        return HttpResponse('User is logged in')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid email or password')
    
    return render(request, 'accounts/login.html')


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def logout(request):
    auth_logout(request)  
    messages.success(request, "You have successfully logged out.")
    return redirect('login')