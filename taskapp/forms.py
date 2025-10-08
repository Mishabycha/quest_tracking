from django.forms import ModelForm, TextInput, Textarea, Select, DateField, DateInput
from taskapp.models import Task

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


