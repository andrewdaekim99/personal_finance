from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

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
