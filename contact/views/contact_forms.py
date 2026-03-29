from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from django import forms

from contact.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = 'first_name', 'last_name', 'phone'


def create(request: WSGIRequest):
    if request.method == 'POST':
        context = {
        'title': 'Create Contact',
        'form': ContactForm(request.POST)
    }
        
        return render(
        request,
        'contact/create.html',
        context
    )

    context = {
        'title': 'Create Contact',
        'form': ContactForm()
    }

    return render(
        request,
        'contact/create.html',
        context
    )