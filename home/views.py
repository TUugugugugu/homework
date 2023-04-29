# hello/views.py

import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import HomeWork
from .forms import NewUserForm, LoginForm, HomeWorkForm
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator



def index(request):
    form = LoginForm()
    message = ""
    user = request.user
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                message = "login success"
            else:
                message = "invalid username or password"
        else:
            message = "invalid username or password"
    return render(request, "home.html", {'form': form, 'message': message, 'user': user})


def register(request):
    form = NewUserForm()
    message = ""
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            message = "Register succesful"
    return render(request, "register.html", {'form': form, 'message': message})


def homeworks(request):
    home_works = HomeWork.objects.filter(created_user = request.user).order_by("deadline")
    paginator = Paginator(home_works, 2)
    page_number = request.GET.get("page")
    homeworks_page = paginator.get_page(page_number)
    return render(request, "homeworks.html", {'homeworks': homeworks_page,})


def homework_add(request):
    form = HomeWorkForm()
    message = ""
    if request.method == "POST":
        form = HomeWorkForm(request.POST, request.FILES)
        if form.is_valid():
            homework = form.save(commit=False)
            homework.created_user = request.user
            homework.created_date = datetime.datetime.now()
            homework.save()
            message = "Homework created successfully"
    return render(request, "homeworks-add.html", {'form': form, 'message': message})

def logout_view(request):
    logout(request)
    return redirect("index")


def homework_edit(request, id):
    homework = HomeWork.objects.get(id=id)
    form = HomeWorkForm(instance=homework)
    message = ""
    if request.method == 'POST':
        form = HomeWorkForm(instance=homework, data=request.POST)
        message = ""
        if form.is_valid():
            form.save()
            message = 'Homework edit done'
    return render(request, 'homeworks-add.html', {'form': form, 'message': message})

def homework_delete(request, id):
    homework = HomeWork.objects.filter(created_user=request.user).filter(id=id)
    homework.delete()
    return redirect("homeworks")


def homework_done(request, id):
    done = request.GET.get('done', False)
    homework = HomeWork.objects.get(id=id)
    homework_done = done
    homework.save()
    return redirect('homeworks')