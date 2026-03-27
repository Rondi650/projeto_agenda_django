from django.shortcuts import render, redirect
from contact.models import Contact
from django.http import Http404
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from rich import print


def index(request: WSGIRequest):
    contacts = Contact.objects.all() \
        .filter(show=True) \
        .order_by('-id')[:10]

    context = {
        'contacts': contacts,
        'title': 'Contatos'
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request: WSGIRequest):
    search_value = request.GET.get('q', '').strip()
    
    if search_value == '':
        return redirect('contact:index')

    contacts = Contact.objects.all() \
        .filter(show=True) \
        .filter(Q(first_name__icontains=search_value) | 
                Q(phone__icontains=search_value) | 
                Q(email__icontains=search_value) | 
                Q(last_name__icontains=search_value)) \
        .order_by('-id')
    
    print(contacts.query)

    context = {
        'contacts': contacts,
        'title': 'Search'
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request: WSGIRequest, contact_id: int):
    single_contact = Contact.objects.filter(
        id=contact_id,
        show=True
    ).first()

    if single_contact is None:
        raise Http404

    context = {
        'contact': single_contact,
        'title': single_contact.last_name
    }

    return render(
        request,
        'contact/contact.html',
        context
    )
