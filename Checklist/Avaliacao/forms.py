# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Avaliacao.models import Categoria, Questao
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
	Questao._meta.get_field('questao').blank = False
	Questao._meta.get_field('Categoria').blank = False
	#Questao._meta.get_field('selectCat').blank = False
	class Meta:
		model = Questao
		fields = ['questao', 'Categoria']
		#Categoria = forms.ModelChoiceField(queryset=None, widget=forms.Select)
		widgets = {
			'questao' : forms.TextInput(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Questão'}),
			'Categoria': forms.Select(attrs={'class' : 'form-control', 'maxlength': 255, 'placeholder': 'Categoria', 'choices': Categoria.objects.values_list('nome').all()}),
		}

	def save(self, commit=True):
		Questao = super(QuestaoModelForm, self).save(commit=False)
		if commit:
			Questao.save()
		return Questao
		
			

