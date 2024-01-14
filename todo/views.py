from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

# Create your views here.

def addTask(request):
    taskadd = request.POST['task']
    Task.objects.create(task=taskadd)
    return redirect('home')