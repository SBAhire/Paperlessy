from django.shortcuts import render,redirect
from django.http import request
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

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
    
    current_category = TaskCategory.objects.get(id=category_id)
    task_form=TaskForm()
    content = {
        
        'title' : current_category.category_name,
        'tasks' : Task.objects.filter(category=current_category).order_by('is_completed'),
        'category_id' : category_id,
        'task_form' : task_form,
    }
    return render(request,'tasks/categorical_list.html',content)

@login_required
def task(request,category_id,task_id):
    task=Task.objects.get(id=task_id)
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
    return redirect('/'+str(category_id)+'/'+str(task_id))

