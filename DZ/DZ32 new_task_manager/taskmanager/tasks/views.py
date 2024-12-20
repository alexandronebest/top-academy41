
from django.shortcuts import render, redirect
from .models import Project, User, Task, TaskStatus
from .forms import TaskForm, TaskCreateForm, ProjectForm

def index(request):
    return render(request, 'index.html')

def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'tasks/list.html', context={'projects': projects_list})

def performers(request):
    performers_list = User.objects.all()
    return render(request, 'tasks/performers.html', context={'performers': performers_list})

def tasks(request):
    tasks_list = Task.objects.all()
    return render(request, 'tasks/tasks.html', context={'tasks': tasks_list})

def project(request, project_id):
    project_view = Project.objects.get(pk=project_id)
    tasks_list = Task.objects.filter(project_id=project_id)  
    return render(request, 'project/details.html', context={'project': project_view, 'tasks': tasks_list})  

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():  # Проверяем корректность формы
            project_view = form.save()  # Создаем проект через форму
            return redirect('project', project_view.id)
    else:
        form = ProjectForm()
    return render(request, 'project/create.html', context={'form': form})

def create_task(request):

    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.status = TaskStatus.objects.get(name="Назначено")
            task.save()
            return redirect('tasks')
    else:
        form = TaskCreateForm()
    projects_list = Project.objects.all()
    return render(request, 'tasks/create.html', context={'form': form, 'projects': projects_list})
def task(request, task_id):
    task_view = Task.objects.get(pk=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_view)
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskForm(instance=task_view)
    return render(request, 'tasks/task/details.html', context={'form': form, 'task': task_view})

