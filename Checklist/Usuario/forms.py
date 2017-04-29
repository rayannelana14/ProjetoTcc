# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django import forms
from Usuario.models import Usuario
from django.db.transaction import commit

class UsuarioModelForm(forms.ModelForm):
    Usuario._meta.get_field('first_name').blank = False
    Usuario._meta.get_field('last_name').blank = False
    Usuario._meta.get_field('email').blank = False
    Usuario._meta.get_field('categoria').blank = False
    class Meta:
        model = Usuario
        fields = ['first_name','last_name', 'email', 'categoria']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 255, 'placeholder': 'Sobrenome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder' : 'Email'}),
            'categoria': forms.Select(attrs={'class': 'form-control', 'maxlength': 18, 'placeholder': 'Selecionar categoria'}),
        }

    def save(self, commit=True):
        Usuario = super(UsuarioModelForm, self).save(commit=False)
        if commit:
            Usuario.save()
        return Usuario