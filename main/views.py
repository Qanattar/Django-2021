from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import *


# Create your views here.


def list_todo_items(request):
    context = {'todo_list': Todo.objects.all()}
    return render(request, 'todo/todo_list.html', context)


def insert_todo_item(request: HttpRequest):
    todo = Todo(content=request.POST['content'])
    todo.save()
    return redirect('/todo_list/')


def delete_todo_item(request, todo_id):
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    return redirect('/todo_list/')


def complete_todo_item(request, todo_id):
    completed_todo = Todo.objects.get(id=todo_id)
    completed = Completed(content=completed_todo.content)
    completed.save()
    todo_to_delete = Todo.objects.get(id=todo_id)
    todo_to_delete.delete()
    context = {'completed_todo_list': Completed.objects.all()}
    return render(request, 'todo/completed_todo.html', context)
