from django.shortcuts import render, redirect
from django.contrib import messages, auth

from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        # Get form values
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            password2 = request.POST['password2']
        except Exception as e:
            print(e)

        # Check whether passwords match
        if password == password2:
            # Check whether username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already in use!')
                return redirect('register')
            else:
                # Check whether email already exists
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email aready in use!')
                    return redirect('register')
                else:
                    # Create user after password, username and email validation is passed
                    user = User.objects.create_user(username=username, password=password, \
                        email=email, first_name=first_name, last_name=last_name)

                    # Login after user registration
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in!')
                    return redirect('index')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    
    return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        try:
            # Get username and password values
            username = request.POST['username']
            password = request.POST['password']
        except Exception as e:
            print(e)

        try:
            # Authenticate using username and password credentials
            user = auth.authenticate(username=username, password=password)
        except Exception as e:
            print(e)
        
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('login')
    
    return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out!')
        return redirect('index')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')
