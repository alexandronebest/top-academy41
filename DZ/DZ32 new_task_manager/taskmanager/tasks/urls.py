from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('projects/', views.projects, name='projects'),
    path('performers/', views.performers, name='performers'),
    path('tasks/', views.tasks, name='tasks'),
    path('projects/create/', views.create_project, name='projects_create'),
    path('project/<int:project_id>/', views.project, name='project'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('signin', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]