from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label='Value 1', required=False, widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label='Value 2',widget=forms.TextInput(attrs={'class':"form-control"}))
    email=forms.EmailField()

from tasks.models import Task  # Ensure Task model is imported correctly

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }