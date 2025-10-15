from django.urls import path 
from .views import TasksListView, TaskCreateView, TaskDeleteView, TaskDetailView, UpdateView

urlpatterns = [
    path('tasks/', TasksListView.as_view(), name='tasks-list'),
    path('tasks/create/', TaskCreateView.as_view(), name='tasks-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='tasks-detail'),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='tasks-delete'),
    path('tasks/update/<int:pk>/', UpdateView.as_view(), name='tasks-update'),
]