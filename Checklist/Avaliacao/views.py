from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from Avaliacao.models import Categoria, Questoes, Checklist, Checklist_Categoria, Avaliacao, Avaliacao_Responsavel
from Avaliacao.forms import CategoriaModelForm, QuestaoModelForm, ChecklistModelForm, AvaliacaoModelForm, RespostaModelForm
from Sistema.models import Sistema
from django.contrib import messages
from django.views.generic import ListView


def checkindex(request):
    return render(request, 'checklist_index.html')

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
	form.fields['Categoria'].choices = [(cat.pk, cat.nome) for cat in Categoria.objects.all()]
	if request.method == 'POST':
		if form.is_valid():	
			form.save()
			messages.success(request, 'Questao cadastrada')
			return redirect('/questao')

	return render(request, 'Avaliacao/questao.html', {'form': form})

	
def checklist(request):
	form = ChecklistModelForm(request.POST or None)
	form.fields['categoria'].choices = [(cat.pk, cat.nome) for cat in Categoria.objects.all()]	
	if request.method == 'POST':
		if form.is_valid():
			print('valido')
			checklist = form.save()
			for cat in form.fields['categoria'].queryset:
				ChkCat = Checklist_Categoria.objects.create(categoria_id = cat.pk, checklist_id= checklist.pk)
				ChkCat.save()
			messages.success(request, 'Checklist cadastrado')
		return redirect('/checklist')
	return render(request, 'Avaliacao/checklist.html', {'form': form})

def avaliacao(request):
	form = AvaliacaoModelForm(request.POST or None)
	form.fields['sistema'].choices = [(sis.pk, sis.nome) for sis in Sistema.objects.all()]
	form.fields['checklist'].choices = [(chk.pk, chk.nome) for chk in Checklist.objects.all()]	
	if request.method == 'POST':
		if form.is_valid():
			avaliacao = form.save()
			for resp in form.fields['responsavel'].queryset:
				responsavel = Avaliacao_Responsavel.objects.create(avaliacao_id = avaliacao.pk, responsavel_id = resp.pk)
				responsavel.save()
			messages.success(request, 'Avaliação cadastrada')
		return redirect('/avaliacao')
	return render(request, 'Avaliacao/avaliacao.html', {'form':form})


def respCheck(request, pk):
	avaliacao = Avaliacao.objects.filter(pk=pk)
	checklist = Avaliacao.objects.filter(pk=pk).values('checklist_id')	
	print(checklist)
	questaoForm = QuestaoModelForm.questao_list()
	respostaForm = RespostaModelForm(request.POST or None)
	return render(request, 'Avaliacao/respCheck.html', {'form': questaoForm, 'formResp': respostaForm, 'pk': pk})


def avaliacao_list(request):
	form = Avaliacao.objects.all()
	return render(request, 'Avaliacao/avaliacao_list.html', {'form': form})

