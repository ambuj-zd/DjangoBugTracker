from django import forms
from .models import Task

class AddStudentForm(forms.ModelForm):
    class Meta :
        model = Task
        fields =("title","tasknum","status","details")
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'tasknum' : forms.NumberInput(attrs={'class':'form-control'}),
            'status' : forms.TextInput(attrs={'class':'form-control'}),
            'details':  forms.TextInput(attrs={'class':'form-control'})
            
        } 