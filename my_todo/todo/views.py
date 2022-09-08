from django.shortcuts import render
from .models import Todo


def index(request):
    context = {
        'todo_list': Todo.objects.all(),
    }
    return render(request, 'todo/index.html', context=context)
