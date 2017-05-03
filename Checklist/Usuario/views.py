from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from Usuario.models import Usuario
from Usuario.forms import UsuarioModelForm
from django.contrib import messages


def index(request):
    return render(request, 'base.html')

def cadastro(request):
    form = UsuarioModelForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/config')

    return render(request,'Usuario/cadastro.html', {'form':form})

