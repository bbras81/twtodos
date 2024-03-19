from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Todo


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["title", "dead_line"]
    success_url = reverse_lazy("todo_list")
