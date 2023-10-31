from django.db import models

# Create your models here.
class TaskList(models.Model):
    title = models.CharField(max_length= 80)
    description = models.TextField()
    status = models.CharField(max_length= 15, default= 'incomplete')