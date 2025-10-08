from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from taskapp import models
# Create your views here.

class TasksListView(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'taskapp/tasks_list.html'
    ordering = ['-created_at']

