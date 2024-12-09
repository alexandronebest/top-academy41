from django.shortcuts import render
from .models import Project, User, Task


def index(request):
  return render(request, 'tasks/index.html')

def projects(request):
  projects_list = Project.objects.all()
  return render(request, 'tasks/projects.html', context={'projects': projects_list})

def performers(request):
  performers_list = User.objects.all()
  return render(request, 'tasks/performers.html', context={'performers': performers_list})

def tasks(request):
  tasks_list = Task.objects.all()
  return render(request, 'tasks/tasks.html', context={'tasks': tasks_list})

def project(request, project_id):
  project_view = Project.objects.get(pk=project_id)
  tasks_list = Task.objects.filter(project_id=project_id)
  return render(request, 'tasks/project.html', context={'project': project_view, 'tasks': tasks_list})