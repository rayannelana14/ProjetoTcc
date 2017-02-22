from django.http import HttpResponse
from django.shortcuts import render
from Usuario.models import Usuario

def cadastro(request):    
    return render(request, 'Usuario\cadastro.html')
		