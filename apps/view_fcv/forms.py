from django import forms
from django.forms import ModelForm
from .models import  Author
class ContactForm(forms.Form):
    name = forms.CharField(label='姓名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='消息', widget=forms.Textarea(attrs={'class': 'form-control'}))

    def print_data(self):
        name = self.cleaned_data['name']
        message = self.cleaned_data['message']
        print('Name is {}, message is {}.'.format(name, message))
class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['name']
        labels = {
            'name': '姓名',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }
    # def save(self, commit=True):
    #     return super().save(commit)
