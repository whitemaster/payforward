from django import forms
from models import Task

class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title','description','category','end_date','task_photo')