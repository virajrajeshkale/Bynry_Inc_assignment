# views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # Custom form to handle registration
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_type = CustomUser.CUSTOMER  # Set user type to Customer
            user.save()
            # print(f"New user created: {user.username}")  # Debugging: print the created user
            login(request, user)  # Automatically log the user in
            return redirect('customer_dashboard')  # Redirect to customer dashboard
        else:
            print(form.errors)  # Debugging: print form errors
    else:
        form = CustomUserCreationForm()
    return render(request, 'base/register.html', {'form': form})




from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            # Redirect based on user type
            if user.user_type == 'customer':
                return redirect('customer_dashboard')
            elif user.user_type == 'support':
                return redirect('support_dashboard')
            else:
                return redirect('customer_dashboard')  # Default to customer dashboard
        else:
            # Form is not valid, including errors
            return render(request, 'base/login.html', {'form': form})
    else:
        form = AuthenticationForm()

    return render(request, 'base/login.html', {'form': form})



# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page after logout


