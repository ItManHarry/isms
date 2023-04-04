from django.forms import ModelForm
from django.db.models import Q
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
        code = cleaned_data['code']
        code_exist = False      # 字典代码是否存在
        try:
            work_book = WordBook.objects.get(pk=id)
        except:
            work_book = None
        if work_book:
            if WordBook.objects.filter(~Q(id=id) & Q(code=code.upper())):
                code_exist = True
        else:
            if WordBook.objects.filter(code=code.upper()):
                code_exist = True
        if code_exist:
            self.add_error('code', '字典代码已存在!')
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