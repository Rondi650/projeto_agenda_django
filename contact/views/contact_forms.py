from django.shortcuts import render
from django.core.handlers.wsgi import WSGIRequest
from contact.forms import ContactForm

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