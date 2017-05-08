from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.forms import UserCreationForm
from Avaliacao.models import Categoria, Questoes, Checklist, Checklist_Categoria, Avaliacao, Avaliacao_Responsavel, Resposta
from Avaliacao.forms import CategoriaModelForm, QuestaoModelForm, ChecklistModelForm, AvaliacaoModelForm, RespostaModelForm
from Sistema.models import Sistema
from django.contrib import messages
from django.views.generic import ListView

def categoria(request):
	form = CategoriaModelForm(request.POST or None)
	context = {'form': form}
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			messages.success(request, 'Categoria cadastrada')
			return redirect('/config')

	return render(request, 'Avaliacao/categoria.html', context)


def questao(request):
	form = QuestaoModelForm(request.POST or None)
	form.fields['Categoria'].choices = [(cat.pk, cat.nome) for cat in Categoria.objects.all()]
	if request.method == 'POST':
		if form.is_valid():	
			form.save()
			messages.success(request, 'Questao cadastrada')
			return redirect('/config')

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
		return redirect('/config')
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
		return redirect('/config')
	return render(request, 'Avaliacao/avaliacao.html', {'form':form})


def respCheck(request, pk):
	avaliacao = Avaliacao.objects.get(pk=pk)
	chk_id = avaliacao.checklist_id
	chkcat = Checklist_Categoria.objects.filter(checklist_id=chk_id)
	categoria = Categoria.objects.all()	
	questaoForm = []
	for obj in chkcat:
		questlist = Questoes.objects.filter(Categoria_id= obj.categoria_id)
		for questao in questlist:
			questaoForm.append(questao)
	respostaForm = RespostaModelForm(request.POST or None)
	if request.method == 'POST':
			if respostaForm.is_valid():
				for questao in questaoForm:
					resp = request.POST.get('resposta')
					resposta = Resposta.objects.create(avaliacao_id= avaliacao.pk, checklist_id=chk_id, questao_id = questao.id, resposta=resp)
					resposta.save()		
			return redirect('/config')
	return render(request, 'Avaliacao/respCheck.html', {'form': questaoForm, 'formResp': respostaForm, 'pk': pk, 'categoria':categoria})




def avaliacao_list(request):
	form = Avaliacao.objects.all()
	return render(request, 'Avaliacao/avaliacao_list.html', {'form': form})


def config(request):	
    return render(request, 'retorno.html')

def checklist_list(request):
	return render(request, 'Avaliacao/checklist_list.html')

def relatorio(request, pk):
	avalist = Avaliacao.objects.filter(sistema_id=pk)
	questoes = []
	sim = 0
	nao = 0
	total = 0
	for avaliacao in avalist:
		catChk = Checklist_Categoria.objects.filter(checklist_id=avaliacao.checklist_id)
		for obj in catChk:
			questlist = Questoes.objects.filter(Categoria_id=obj.categoria_id).order_by()
			for questao in questlist:
				categoria = Categoria.objects.get(pk=obj.categoria_id)
				resposta = Resposta.objects.filter(questao_id=questao.pk)
				for resp in resposta:
					if resp.resposta == 'Sim':
						sim = sim + 1
					elif resp.resposta == 'Nao':
						nao = nao + 1
					total = total + 1
			na = total - (sim + nao)
			sim = (sim * 100)/total	
			nao = (nao * 100)/total
			questoes.append({'categoria': categoria.nome, 'sim': sim, 'nao': nao, 'na': na, 'avaliacao':avalist})
			sim = nao = total = 0
	return render(request, 'Avaliacao/relatorio.html', {'questoes':questoes, 'pk': pk})












