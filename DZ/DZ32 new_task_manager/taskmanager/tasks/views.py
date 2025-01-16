from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Project, User, Task
from .forms import TaskForm, TaskCreateForm, ProjectForm, SignupForm

def index(request):
    return render(request, 'index.html')

@login_required
def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'tasks/list.html', context={'projects': projects_list})

@login_required
def performers(request):
    performers_list = User.objects.all()
    return render(request, 'tasks/performers.html', context={'performers': performers_list})

@login_required
def tasks(request):
    tasks_list = Task.objects.all()
    return render(request, 'tasks/tasks.html', context={'tasks': tasks_list})

@login_required
def project(request, project_id):
    project_view = get_object_or_404(Project, pk=project_id)
    tasks_list = Task.objects.filter(project_id=project_id)  
    return render(request, 'project/details.html', context={'project': project_view, 'tasks': tasks_list})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():  # Проверяем корректность формы
            project_view = form.save()  # Создаем проект через форму
            return redirect('project', project_view.id)
    else:
        form = ProjectForm()
    return render(request, 'project/create.html', context={'form': form})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()  # Сохраняем задачу через форму
            return redirect('tasks')
    else:
        form = TaskCreateForm()
    
    projects_list = Project.objects.all()
    return render(request, 'tasks/create.html', context={'form': form, 'projects': projects_list})

@login_required
def task(request, task_id):
    task_view = get_object_or_404(Task, pk=task_id)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_view)
        if form.is_valid():
            form.save()  # Сохраняем изменения задачи
            return redirect('tasks')
    else:
        form = TaskForm(instance=task_view)

    return render(request, 'tasks/task/details.html', context={'form': form, 'task': task_view})

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Хэшируем пароль
            user.save()
            return redirect('signin')
    else:
        form = SignupForm()
    
    return render(request, 'auth/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)  # Аутентификация пользователя
        
        if user is not None:
            login(request, user)  # Вход пользователя
            return redirect('index')  # Перенаправление после успешного входа
        else:
            return render(request, 'auth/signin.html', {'error': 'Неверный логин или пароль'})
    
    return render(request, 'auth/signin.html')

def signout(request):
    logout(request)  # Выход из системы
    return redirect('signin')  # Перенаправление на страницу входа