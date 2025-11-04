from django.forms import ModelForm, TextInput, Textarea, Select, DateField, DateInput, FileInput, Form, ChoiceField
from taskapp.models import Task, Comment

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "description", "status", "priority", "due_date"]

        widgets = {
            "name": TextInput(attrs={"class": "form-control", "placeholder": "Назва задачі", "required": True}),
            "description": Textarea(attrs={"class": "form-control", "placeholder": "Опис задачі", "required": True}),
            "status": Select(attrs={"class": "form-control", "required": True}),
            "priority": Select(attrs={"class": "form-control", "required": True}),
            "due_date": DateInput(attrs={"class": "form-control", "required": False, "type": "date"})

        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content", "media"]

        widgets = {
            "content": Textarea(attrs={"class": "form-control", "placeholder": "Текст коментарю", "required": True}),
            "media": FileInput(attrs={"class": "form-control", "required":False})
        }

class TasksFilterForm(Form):
    STATUS_CHOICES = [
        ("", "Всі"),
        ("todo", "TO DO"),
        ("in_progress", "IN PROGRESS"),
        ("done", "DONE"),
    ]

    PRIORITY_CHOICES = [
        ("", "Всі"),
        ("low", "LOW"),
        ("medium", "MEDIUM"),
        ("high", "HIGH"),
    ]

    status = ChoiceField(choices=STATUS_CHOICES, required=False, label="Статус", widget=Select(attrs={"class": "form-control"}))
    priority = ChoiceField(choices=PRIORITY_CHOICES, required=False, label="Пріорітет", widget=Select(attrs={"class": "form-control"}))

