from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from Avaliacao.models import Categoria, Questao
from Avaliacao.forms import CategoriaModelForm, QuestaoModelForm
from django.contrib import messages
from django.views.generic import ListView

def categoria(request):
	form = CategoriaModelForm(request.POST or None)
	context = {'form': form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'Categoria cadastrada')
			return redirect('/categoria')

	return render(request, 'Avaliacao/categoria.html', context)


def questao(request):
	form = QuestaoModelForm(request.POST or None)
	context = {'form': form}
	form['Categoria'].queryset=Categoria.objects.values_list('nome').all()
	if request.method == 'POST':		
		print('if method')
		#print(form)
		if form.is_valid():					
			print('if valid')			
			print(form)		
			form.save()
			messages.success(request, 'Questao cadastrada')
			return redirect('/questao')

	return render(request, 'Avaliacao/questao.html', {'form': form})

	class ListadeCategoria(ListView):
		model = Avaliacao