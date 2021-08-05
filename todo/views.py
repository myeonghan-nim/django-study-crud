from django.shortcuts import render, redirect

from .models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index.html', context)


def detail(request, id):
    context = {
        'todo': Todo.objects.get(id=id),
    }
    return render(request, 'detail.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    Todo(
        title=request.GET.get('title'),
        due_date=request.GET.get('duedate')
    ).save()
    return redirect('/todos/')


def delete(request, id):
    Todo.objects.get(id=id).delete()
    return redirect('/todos/')


def edit(request, id):
    context = {
        'todo': Todo.objects.get(id=id),
    }
    return render(request, 'edit.html', context)


def update(request, id):
    todo = Todo.objects.get(id=id)
    todo.title = request.GET.get('title')
    todo.due_date = request.GET.get('duedate')
    todo.save()
    return redirect('/todos/')
