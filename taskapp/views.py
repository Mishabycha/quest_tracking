from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from taskapp import forms, models
from django.urls import reverse_lazy
from taskapp.mixins import UserIsOwnerMixin
# Create your views here.

class TasksListView(ListView):
    model = models.Task
    context_object_name = 'tasks'
    template_name = 'taskapp/tasks_list.html'
    ordering = ['-created_at']

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'taskapp/tasks_create.html'
    success_url = reverse_lazy("tasks-list")

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    
class UpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = models.Task
    form_class = forms.TaskForm
    template_name = 'taskapp/tasks_update.html'
    success_url = reverse_lazy("tasks-list")

class TaskDetailView(DetailView):
    model = models.Task
    context_object_name = "task"
    template_name = 'taskapp/tasks_detail.html'

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Task
    template_name = 'taskapp/tasks_delete.html'
    success_url = reverse_lazy("tasks-list")

