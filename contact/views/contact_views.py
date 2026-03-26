from django.shortcuts import render
from contact.models import Contact
from django.http import Http404


def index(request):
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


def contact(request, contact_id):
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
