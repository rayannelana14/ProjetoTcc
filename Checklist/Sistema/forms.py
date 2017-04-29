# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Sistema.models import Sistema
from django.db.transaction import commit

class SistemaModelForm(forms.ModelForm):
    Sistema._meta.get_field('requisitos').blank = False
    Sistema._meta.get_field('metas').blank = False
    Sistema._meta.get_field('categoria').blank = False
    Sistema._meta.get_field('nome').blank = False
    Sistema._meta.get_field('empresa').blank = False
    Sistema._meta.get_field('projeto').blank = False
    class Meta:
        model = Sistema
        fields = ['requisitos', 'metas', 'categoria','nome', 'empresa','projeto']
        widgets = {
            'requisitos': forms.TextInput(attrs={'class':'form-control', 'maxlength': 100, 'placeholder': 'Requisitos'}),
            'metas': forms.NumberInput(attrs={'class': 'form-control', 'maxlength': 5, 'placeholder': 'Meta'}),
            'categoria': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 30, 'placeholder': 'Categoria do Sistema'}),
            'nome' : forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': 'Nome'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': 'Empresa'}),
            'projeto': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 50, 'placeholder': 'Projeto'}),
        }

    def save(self, commit=True):
        Sistema = super(SistemaModelForm, self).save(commit=False)
        if commit:
            Sistema.save()
        return Sistema

