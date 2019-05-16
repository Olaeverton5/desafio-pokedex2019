from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def mostrarPokemons(request):
    pokemons = Pokemon.objects.all()

    contexto = {
        "todos_pokemons": pokemons,
        "usuario": "stefan",
        "data_atual": "16/05/2019"
    }
    return render(request, 'basico.html', contexto)

@csrf_exempt
def salvarCategoria(request):
    if request.method == "POST":
        if 'nome' in request.POST:
            Categoria.objects.create(nome=request.POST['nome'])

            return HttpResponse("Inseriu",)
        return HttpResponse("FOI POST EM BRANCO")
    return HttpResponse("NÃO FOI POST")