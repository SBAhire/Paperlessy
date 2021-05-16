from rest_framework import serializers
from .models import Task, TaskCategory

# Category Serializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskCategory
        fields = '__all__'

# Task Serializer

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
