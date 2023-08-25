from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
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
            return redirect('success')
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
