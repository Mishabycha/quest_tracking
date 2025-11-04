from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("todo", "TO DO"),
        ("in_progress", "IN PROGRESS"),
        ("done", "DONE"),
    ]

    PRIORITY_CHOICES = [
        ("low", "LOW"),
        ("medium", "MEDIUM"),
        ("high", "HIGH"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default="todo")
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=20, default="low")
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Comment(models.Model):
    content = models.TextField(max_length=255)
    media = models.FileField(upload_to="comment_media", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
