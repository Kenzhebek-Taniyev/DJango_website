from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'main/index.html', {'title': 'Home page', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def addTask(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is invalid'

    form = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/addTask.html', context)