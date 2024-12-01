from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    model = Task
    class Meta:
        fields = ["content", "deadline", "status", "tags"]


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
