# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Avaliacao.models import Categoria, Questoes, Checklist
from Usuario.models import Usuario
from django.db.transaction import commit

class CategoriaModelForm(forms.ModelForm):
	Categoria._meta.get_field('nome').blank = False
	Categoria._meta.get_field('descricao').blank = False
	class Meta:
		model = Categoria
		fields = ['nome', 'descricao']
		widgets = {
			'nome' : forms.TextInput(attrs={'class': 'form-control', 'maxlength': 150, 'placeholder': 'Nome'}),
			'descricao' : forms.TextInput(attrs={'class': 'form-control', 'maxlength': 180, 'placeholder': 'Descrição'})
		}
	
	def save(self, commit=True):
		Categoria = super(CategoriaModelForm, self).save(commit=False)
		if commit:
			Categoria.save()
		return Categoria

class QuestaoModelForm(forms.ModelForm):
	Questoes._meta.get_field('questao').blank = False
	Questoes._meta.get_field('diretrizes').blank = False
	Questoes._meta.get_field('Categoria').blank = False
	class Meta:
		model = Questoes
		fields = ['questao', 'diretrizes', 'Categoria']
		choice = [(cat.pk, cat.nome) for cat in Categoria.objects.all()]
		widgets = {		
            'questao' : forms.TextInput(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Questão'}),
            'diretrizes' : forms.TextInput(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Diretrizes'}),
            'Categoria': forms.Select(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Categoria'},choices=choice),             
        	     
		}

	def save(self, commit=True):
		Questao = super(QuestaoModelForm, self).save(commit=False)
		if commit:
			Questao.save()
		return Questao
		
class ChecklistModelForm(forms.ModelForm):
	Checklist._meta.get_field('nome').blank = False
	Checklist._meta.get_field('descricao').blank = False
	Checklist._meta.get_field('especialista').blank = False
	Checklist._meta.get_field('categoria').blank = False
	class Meta:
		model = Checklist
		fields = ['nome', 'descricao', 'especialista', 'categoria']
		choice = [(elab.pk, elab) for elab in Usuario.objects.filter(categoria='ESPECIALISTA')]
		options = [(cat.pk, cat.nome) for cat in Categoria.objects.all()]
		widgets = {
			'nome' : forms.TextInput(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Nome'}),
			'descricao' : forms.TextInput(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Descrição'}),
			'especialista' : forms.Select(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Especialista'},choices=choice),
			'categoria' : forms.CheckboxSelectMultiple(choices=options),
			#'categoria' : forms.RadioSelect(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Especialista'},choices=options),
		}

	def save(self, commit=True):
		Checklist = super(ChecklistModelForm, self).save(commit=False)
		if commit:
			Checklist.save()
		return Checklist

