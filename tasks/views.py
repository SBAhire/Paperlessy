from django.shortcuts import render,redirect
from django.http import request
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from random import choice
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

@login_required
def index(request):
    categories = TaskCategory.objects.filter(created_by=request.user)

    if request.method=='POST':
        category_form=CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            category_form.save()
            return redirect('/')

    category_form = CategoryForm()

    content = {
        'title' : "Sticky Notes",
        'categories' : categories,
        'category_form' : category_form,
    }
    return render(request,'tasks/index.html',content)

@login_required
def categorical_list(request,category_id):
    if request.method=="POST":
        task_form=TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            redirect('/'+str(category_id))
    try:
        current_category = TaskCategory.objects.get(id=category_id)
    except Exception:
        return redirect('/')
    task_form=TaskForm()
    colors=["#eedd82","#cfead9","#f7d98a","#fffd80","#ffc7fe","#c7f1ff","#a5ff61"]
    
    content = {
        
        'title' : current_category.category_name,
        'tasks' : Task.objects.filter(category=current_category).order_by('is_completed','-created_on'),
        'category_id' : category_id,
        'task_form' : task_form,
        'bg_color' : colors,
    }
    return render(request,'tasks/categorical_list.html',content)

@login_required
def task(request,category_id,task_id):
    try:
        task=Task.objects.get(id=task_id)
    except Exception:
        return redirect('/'+str(category_id))
    task_form=TaskForm(instance=task)

    if request.method=='POST':
        task_form=TaskForm(request.POST,instance=task)
        print(task_form)
        if task_form.is_valid():
            task_form.save()
        redirect('/'+str(category_id)+'/'+str(task_id))

    content = {
        'title' : task.task_name,
        'task' : task,
        'category_id' : category_id,
        'task_form' : task_form,
    }
    return render(request,'tasks/task.html',content)

@login_required
def delete_category(request,category_id):
    TaskCategory.objects.filter(id=category_id).delete()
    return redirect('/')

@login_required
def delete_task(request,category_id,task_id):
    Task.objects.filter(id=task_id).delete()
    return redirect('/'+str(category_id))

@login_required
def mark_task_as_complete(request,category_id,task_id):
    current_task = Task.objects.get(id=task_id)
    if current_task.is_completed:
        current_task.is_completed = False
    else:
        current_task.is_completed = True
    current_task.save()
    return redirect('/'+str(category_id))

@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'CategoryList':'/categories',
        'TaskList':'/<int:category_id>/',
        'Task':'/<int:category_id>/<int:task_id>',
        'CreateCategory':'/create-category/',
        'DeleteCategory':'/delete-category/<int:category_id>',
        'CreateTask':'/<int:category_id>/create-task/',
        'DeleteTask':'/<int:category_id>/delete-task/<int:task_id>',
    }
    return Response(api_urls)

@login_required
@api_view(['GET'])
def api_category_list(request):
    categories = TaskCategory.objects.filter(created_by=request.user)
    serializer = CategorySerializer(categories,many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def api_tasks(request,category_id):
    tasks = Task.objects.filter(category=category_id).order_by('is_completed','-created_on')
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

@login_required
@api_view(['GET'])
def api_task(request,category_id,task_id):
    return Response(TaskSerializer(Task.objects.get(id=task_id),many=False).data)

@login_required
@api_view(['POST'])
def api_create_category(request):
    user_data = request.data
    user_data['created_by']=request.user.id

    serializer = CategorySerializer(data=user_data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@login_required
@api_view(['DELETE'])
def api_delete_category(request,category_id):
    current_category = TaskCategory.objects.get(id=category_id)
    if current_category.created_by.id == request.user.id:
        current_category.delete()
        return Response("Category Successfully Deleted")
    return Response("This doesn't exist")

@login_required
@api_view(['POST'])
def api_create_task(request,category_id):
    if TaskCategory.objects.get(id=category_id).created_by.id != request.user.id:
        return Response("Invalid category")
    category_data=request.data
    category_data['category']=category_id
    category_data['is_completed']=False
    serializer = TaskSerializer(data=category_data)

    if serializer.is_valid():
        serializer.save()
        
        return Response(serializer.data)
    return Response("Invalid Content")


@login_required
@api_view(['DELETE'])
def api_delete_task(request,category_id,task_id):
    if TaskCategory.objects.get(id=category_id).created_by.id != request.user.id:
        return Response("Invalid Task")
    Task.objects.get(id=task_id).delete()
    return Response("Task successfully deleted")

    


def tp_view(request):
    return render(request,'tasks/tp.html')



