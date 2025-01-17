
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Project, Task, User, TaskStatus

admin.site.site_header = "Управление проектами"
admin.site.site_title = "Админка Task Manager"
admin.site.index_title = "Добро пожаловать в Task Manager"

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'due_date', 'project')  # Поля для отображения в списке
    list_filter = ('status', 'project')  # Фильтры в правой части админки
    search_fields = ('title', 'description')  # Поля для поиска
    ordering = ('due_date',)  # Сортировка записей

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')  # Поля для отображения в списке

@admin.register(User)
class UserAdmin(BaseUserAdmin):  # Используем BaseUserAdmin как базовый класс
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_staff')  

    # Определяем fieldsets без дублирования полей
    fieldsets = (
        (None, {'fields': ('username', 'password')}),  # Поля для аутентификации
        ('Личная информация', {'fields': ('first_name', 'last_name', 'email')}),  # Личная информация
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),  # Права доступа
        ('Даты', {'fields': ('last_login', 'date_joined')}),  # Даты
    )


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля, по которым можно будет искать
    list_filter = ('name',)  # Фильтры для списка