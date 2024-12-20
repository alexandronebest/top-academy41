from django import forms
from .models import Task, Project

class TaskCreateForm(forms.ModelForm):
  class Meta:
    model = Task
    fields = ['project', 'title', 'description', 'due_date']
  
    widgets = {
      'project': forms.Select(attrs={
        'class': 'form-select',
        'id': 'floatingProjectSelect',
        'aria-label': 'Выбор проекта для привязки задачи',
        'required': True
      }),
      'title': forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingTitle',
        'placeholder': 'Очень простая задача',
        'required': True
      }),
      'description': forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'floatingDescription',
        'placeholder': 'Нужно сделать несколько пунктов...',
        'required': True
      }),
      'due_date': forms.DateInput(attrs={
        'class': 'form-control',
        'id': 'floatingDueDate',
        'type': 'date',
        'required': True
      }),
    }


class TaskForm(forms.ModelForm):
     class Meta:
        model = Task
        fields = ['project', 'title', 'description', 'due_date', 'status']  # Все поля, которые можно редактировать
        widgets = {
           'project': forms.Select(attrs={'class': 'form-select'}),
           'title': forms.TextInput(attrs={'class': 'form-control'}),
           'description': forms.TextInput(attrs={'class': 'form-control'}),
           'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
           'status': forms.Select(attrs={'class': 'form-select'}),
           }
        

class ProjectForm(forms.ModelForm):
     class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'description': forms.TextInput(attrs={'class': 'form-control'}),
           }