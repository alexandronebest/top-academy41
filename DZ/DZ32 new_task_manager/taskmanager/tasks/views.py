from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .models import Project, Task, TaskStatus
from .forms import ProjectForm, TaskCreateForm, TaskForm, SignupForm

@login_required
def project(request, project_id):
    project_view = get_object_or_404(Project, pk=project_id)  # Используем get_object_or_404 для обработки ошибок
    tasks_list = Task.objects.filter(project_id=project_id)
    return render(request, 'project/details.html', context={'project': project_view, 'tasks': tasks_list})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
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
            task = form.save(commit=False)
            task.status = TaskStatus.objects.get(name="Назначено")  # Убедитесь, что этот статус существует
            task.save()
            return redirect('tasks')
    else:
        form = TaskCreateForm()

    projects_list = Project.objects.all()
    return render(request, 'tasks/create.html', context={'form': form, 'projects': projects_list})

@login_required
def task(request, task_id):
    task_view = get_object_or_404(Task, pk=task_id)  # Обрабатываем исключения
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task_view)
        if form.is_valid():
            form.save()
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

        # Аутентификация пользователя
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Вход пользователя
            return redirect('index')  # Перенаправление после успешного входа
        else:
            # Ошибка входа
            return render(request, 'auth/signin.html', {'error': 'Неверный логин или пароль'})

    return render(request, 'auth/signin.html')

def signout(request):
    # Выходим из системы
    logout(request)
    # Перенаправляем пользователя на страницу входа
    return redirect('signin')