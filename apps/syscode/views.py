from django.shortcuts import render, redirect, reverse
from .models import WordBook, WordEnum
from .forms import WordBookForm, WordEnumForm
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
def wordenum_add(request, book_id):
    wordbook = WordBook.objects.get(pk=book_id)
    enums = wordbook.wordenum_set.order_by('code').all()
    if request.method == 'POST':
        form = WordEnumForm(request.POST)
        if form.is_valid():
            enum = form.save(commit=False)
            enum.word_book = wordbook
            enum.save()
            return redirect(reverse('syscode:wordenum_add', args=(book_id, )))
    else:
        form = WordEnumForm()
    return render(request, 'wordbook/enums.html', context=dict(enums=enums, form=form, wordbook=wordbook))

def wordenum_edit(request, book_id, enum_id):
    wordbook = WordBook.objects.get(pk=book_id)
    enums = wordbook.wordenum_set.order_by('code').all()
    enum = WordEnum.objects.get(pk=enum_id)
    if request.method == 'POST':
        form = WordEnumForm(request.POST, instance=enum)
        if form.is_valid():
            enum = form.save(commit=False)
            enum.updated_on = timezone.now()
            enum.save()
            return redirect(reverse('syscode:wordenum_edit', args=(book_id, enum_id, )))
    else:
        form = WordEnumForm(instance=enum)
    return render(request, 'wordbook/enums.html', context=dict(enums=enums, form=form, wordbook=wordbook))