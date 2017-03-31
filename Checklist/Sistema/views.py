from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from Sistema.models import Sistema
from Sistema.forms import SistemaModelForm
from django.contrib import messages

def cadastroSistema(request):
	print('Entrei no metodo')
	form = SistemaModelForm(request.POST or None)
	context = {'form':form}
	print('Testando metodo')
	if request.method == 'POST':
		print('Vou testar o formulario')
		print(form)
		if form.is_valid():
			print('salvando')
			form.save()
			messages.success(request, 'Sistema Cadastrado')
			return redirect ('/cadastroSistema')

	print('Montando a tela')
	return render(request, 'Sistema/sistema.html', context)