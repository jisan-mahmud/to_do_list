from django.contrib import admin
from .models import TaskList
# Registier your models here.

@admin.register(TaskList)
class TaskLIstAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'status']