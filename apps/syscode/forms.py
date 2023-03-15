from django.forms import ModelForm
from django import forms
from .models import WordBook, WordEnum
class WordBookForm(ModelForm):
    class Meta:
        model = WordBook
        fields = ['name', 'code']
        labels = {
            'code': '字典代码',
            'name': '字典名称',
        }
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'disabled': True, 'placeholder': '系统自动生成!'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }
