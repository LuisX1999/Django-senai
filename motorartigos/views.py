from django.shortcuts import render
from django.http import HttpResponse
# CORREÇÃO 1: Sintaxe correta do import do Python
from motorartigos.models import Autor


# Create your views here.
def index(request):
    autores = Autor.objects.all()
    return render (request, 'motorartigos/index.html', {'autores': autores} )

def artigo(request):
    return render (request, 'motorartigos/artigo.html')