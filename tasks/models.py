from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskCategory(models.Model):
    category_name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.category_name

class Task(models.Model):
    category=models.ForeignKey(to=TaskCategory,on_delete=models.CASCADE)
    task_name=models.CharField(max_length=200)
    created_on=models.DateTimeField(auto_now_add=True)
    is_completed=models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
    
