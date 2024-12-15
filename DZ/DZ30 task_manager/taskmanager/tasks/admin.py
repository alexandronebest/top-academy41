from django.contrib import admin

from tasks.models import Project, Task, User, TaskStatus


admin.site.register(Project)
admin.site.register(Task)
admin.site.register(User)
admin.site.register(TaskStatus)