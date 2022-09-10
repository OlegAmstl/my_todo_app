from typing import Any
from django.shortcuts import render

from .models import Todo


def index(request) -> Any:
    '''Рендер главной страницы.'''
    
    context: dict = {
        'todo_list': Todo.objects.all(),
    }
    return render(request, 'todo/index.html', context=context)
