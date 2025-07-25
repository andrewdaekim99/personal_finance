from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # 1. Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'tracker/register.html')
        
        # 2. Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return render(request, 'tracker/register.html')
        
        # 3. Create the user
        user = User.objects.create_user(username=username, password=password)
        user.save()

        messages.success(request, "Account created! You can now log in.")
        return redirect('login') # use the name of login URL pattern
    
    return render(request, 'tracker/register.html')

def login_view(request):
    # redirect if user is already logged in
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # 1. Authenticate the credentials
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # 2. if Authentication is successful, log in and redirect to dashboard
            login(request, user)
            return redirect('dashboard')
        else:
            # if invalid, show error message
            messages.error(request, "Credentials are invalid")
            return render(request, 'tracker/login.html')


    return render(request, 'tracker/login.html')

@login_required
def logout_view(request):
    # log out the user and redirect to logout page
    logout(request)
    return redirect('login')
