from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def mostrarPokemons(request):
    pokemons = Pokemon.objects.all()

    contexto = {
        "todos_pokemons": pokemons,
    }
    return render(request, 'listar.html', contexto)

def mostrarPokemon(request):
    pokemon = Pokemon.objects.all().first()

    contexto = {
        "pokemon": pokemon,
    }
    return render(request,'pokemon.html',contexto)

@csrf_exempt
def salvarCategoria(request):
    if request.method == "POST":
        if 'nome' in request.POST:
            Categoria.objects.create(nome=request.POST['nome'])

            return HttpResponse("Inseriu",)
        return HttpResponse("FOI POST EM BRANCO")
    if request.method == "GET":
        return HttpResponse("Não aceito get")
    return HttpResponse("NÃO FOI POST")