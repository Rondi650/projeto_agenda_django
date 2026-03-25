from django.shortcuts import render

def index(request):
    return render(
        request,
        'contact/index.html',
        context= {
            "title": 'index',
            "exemplo": "Esse e um texto de exemplo para a pagina",
            "outro_exemplo": 'Outro texto de exemplo'
        }
    )

