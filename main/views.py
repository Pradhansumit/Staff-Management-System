from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from . import models
from . import forms

# homepage


def index(request):
    return render(request, 'main/index.html')


# signup/registration function
def signup(request):
    if request.method == 'POST':
        form = forms.UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
            raise ValueError('Login Failed')
    else:
        form = forms.UserCreationForm()
    return render(request, 'main/signup.html', locals())

# login function


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)

        if user is not None:
            auth_login(request, user)
            # return redirect('success')
            if user.is_superuser:
                return redirect('admin_dashboard')
        else:
            raise ValueError("Put correct credentials")
    else:
        return render(request, 'main/login.html')

# logout function


def logout(request):
    auth_logout(request)
    return redirect('login')


@login_required
def timer(request):
    return render(request, 'main/timer.html')


@login_required
def timerStart(request):
    if request.method == 'GET':
        start_model = models.StartTime.objects.create(user=request.user)
    return redirect('success')


@login_required
def timerStop(request):
    if request.method == "GET":
        stop_model = models.StopTime.objects.create(user=request.user)
    return redirect('success')


def timeSheetUpdate(request):
    if request.method == 'GET':
        user = request.user
        start_time = models.StartTime.objects.latest('start_time')
        stop_time = models.StopTime.objects.latest('stop_time')
        models.TimeSheet.objects.create(
            user=user, start_time=start_time, stop_time=stop_time)
        return JsonResponse({'status': 'success'})


def success(request):
    return render(request, 'main/success.html')

# admin actions


@login_required
def admin_dashboard(request):
    user = request.user
    timesheet_models = models.TimeSheet.objects.all()
    return render(request, 'main/admin_dashboard.html', locals())

# admin search action


def adminSearch(request):
    if request.method == 'GET':
        search_name = request.GET['search-name']
        print(search_name)
        searched_user = models.CustomUserModel.objects.get(name=search_name)
        user_id = searched_user.id
        user_time = models.TimeSheet.objects.filter(user=user_id)
        return render(request, 'main/searched.html', locals())
