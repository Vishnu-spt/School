# views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import Department, Course, Order, Material
from .forms import LoginForm, RegisterForm, OrderForm

def home(request):
    departments = Department.objects.all()
    return render(request, 'home.html', {'departments': departments})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Login successful!')
                user.save()
                return redirect('new_page')
            else:
                messages.error(request, 'Invalid login credentials.')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration successful!')
            form.save()
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# schoolapp/views.py

def new_page(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Add order processing logic here
            messages.success(request, 'Order Confirmed!')
            return redirect('home')
    else:
        # Initialize the form with department data if available
        department_id = request.GET.get('department_id')  # Adjust this based on your URL structure
        form = OrderForm(initial={'department': department_id})

        # Set department choices for the form
        form.fields['course'].queryset = Course.objects.none()

        if 'department' in request.GET:
            try:
                department_id = int(request.GET.get('department'))
                form.fields['course'].queryset = Course.objects.filter(department_id=department_id)
            except (ValueError, TypeError):
                pass
        elif form.instance and hasattr(form.instance, 'department'):
            form.fields['course'].queryset = form.instance.department.course_set.all()

    return render(request, 'new_page.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')
