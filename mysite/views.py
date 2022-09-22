# filename: views.py (Django view functions)

from django.http import HttpResponse


def index(request):
    # Get an HttpRequest - the request parameter
    # perform operations using information from the request.
    # Return HttpResponse
    return HttpResponse('Hello from Django!')

# favor utilizar o código acima no seu projeto ao invés do que está abaixo
# nome do arquivo: views.py (Onde as funções view ficam)


def index(requisito):
    # Recebe um HttpRequest - o parametro requisito
    # Executar operações usando informações do requisito (solicitação).
    # Retornar HttpResponse
    return HttpResponse('Um oi do Django!')
