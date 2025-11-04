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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter_form"] = forms.TasksFilterForm(self.request.GET)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status")
        priority = self.request.GET.get("priority")

        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = forms.CommentForm()
        return context
    
    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect("tasks-detail", pk=comment.task.pk)
        else:
            pass


class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = models.Task
    template_name = 'taskapp/tasks_delete.html'
    success_url = reverse_lazy("tasks-list")

