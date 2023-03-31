from django.forms import ModelForm
from django import forms
from .models import WordBook, WordEnum
class WordBookForm(ModelForm):
    class Meta:
        model = WordBook
        fields = ['name', 'code', 'id']
        labels = {
            'code': '字典代码',
            'name': '字典名称',
        }
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'id': forms.HiddenInput(),
        }
    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data['id']
        work_book = WordBook.objects.filter(id=id)
        if work_book:
            print('Edit....................')
        else:
            print('Add.....................')
class WordEnumForm(ModelForm):
    class Meta:
        model = WordEnum
        fields = ['name', 'code']
        labels = {
            'code': '枚举代码',
            'name': '枚举名称',
        }
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }