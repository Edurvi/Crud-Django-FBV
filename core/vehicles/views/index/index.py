from django.shortcuts import render


def index(request):
    template_name = 'index/index.html'
    context = {
        'Mensaje': 'Hola Mundo'
    }
    return render(request, template_name, context)


