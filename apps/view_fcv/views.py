from django.shortcuts import render, reverse
from django.views.generic.edit import FormView
from .forms import ContactForm, AuthorForm
class ContactFormView(FormView):
    template_name = 'fcv/contact.html'
    form_class = ContactForm
    success_url = '/view_fcv/contact/'

    def form_valid(self, form):
        form.print_data()
        return super().form_valid(form)
class AuthorFormView(FormView):
    template_name = 'fcv/author.html'
    form_class = AuthorForm
    success_url = '/view_fcv/author/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
