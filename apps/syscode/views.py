from django.shortcuts import render, redirect, reverse
from .models import WordBook, WordEnum
from .forms import WordBookForm
from django.utils import timezone

def wordbook_index(request):
    books = WordBook.objects.all()
    return render(request, 'wordbook/index.html', context=dict(books=books))
def wordbook_add(request):
    if request.method == 'POST':
        form = WordBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('syscode:wordbook_add'))
    else:
        form = WordBookForm()
    return render(request, 'wordbook/edit.html', context=dict(form=form, title='新增字典'))
def wordbook_edit(request, id):
    wordbook = WordBook.objects.get(pk=id)
    if request.method == 'POST':
        form = WordBookForm(request.POST, instance=wordbook)
        if form.is_valid():
            wordbook = form.save(commit=False)
            wordbook.updated_on = timezone.now()
            wordbook.save()
            return redirect(reverse('syscode:wordbook_edit', args=(id,)))
    else:
        form = WordBookForm(instance=wordbook)
    return render(request, 'wordbook/edit.html', context=dict(form=form, title='编辑字典'))