from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from Sistema.models import Sistema
from Sistema.forms import SistemaModelForm
from django.contrib import messages

def cadastroSistema(request):
	form = SistemaModelForm(request.POST or None)
	context = {'form':form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'Sistema Cadastrado')
			return redirect ('/cadastroSistema')
	return render(request, 'Sistema/sistema.html', context)

def sistema_list(request):
	form = Sistema.objects.all()
	return render(request, 'Sistema/sistema_list.html', {'form':form})