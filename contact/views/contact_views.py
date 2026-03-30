from django.shortcuts import render, redirect
from contact.models import Contact
from django.http import Http404
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import Q
from django.core.paginator import Paginator


def index(request: WSGIRequest):
    contacts = Contact.objects.all() \
        .filter(show=True) \
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
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
    print(single_contact)

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
