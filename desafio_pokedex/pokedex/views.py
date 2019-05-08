from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon

# Create your views here.

def mostrarPokemons(request):
    pokemons = Pokemon.objects.all()

    contexto = {
        "todos_pokemons": pokemons
    }
    return render(request,'basico.html',contexto)