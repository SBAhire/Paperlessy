from django.forms import ModelForm

from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = TaskCategory
        fields = '__all__'


