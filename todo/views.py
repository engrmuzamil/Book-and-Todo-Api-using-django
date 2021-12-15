from django.shortcuts import render
from .models import Todo
from django.views.generic import ListView
# Create your views here.
class todoView(ListView):
    model = Todo
    template_name = "todo/home.html"
    context_object_name = "Todos"
