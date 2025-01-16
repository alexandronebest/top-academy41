from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
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
class UserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительная информация', {'fields': ('first_name', 'last_name')}),
        )