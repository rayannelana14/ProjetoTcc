from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.contrib.auth.forms import UserCreationForm
from Usuario.models import Usuario

#pagina inicial
def index(request):
	return render_to_response("index.html")

#pagina de cadastro de Usuario
def cadastro(request):      
    #Se dados forem passados via POST
	if request.method == 'POST': 
		#form = UserCreationForm(request.POST)
		f = ArticleForm(request.POST)
		new_article = f.save()
		a = Article.objects.get(pk=1)
		f = ArticleForm(request.POST, instance=a)
		f.save()

		#Testa se o formulario é válido
		#if form.is_valid():
		#	form.save()
		#	return HttpResponseRedirect("login.html")
		#if form.is_valid():
		return HttpResponseRedirect("login.html")
		#else:
			#mostra novamente o formulario de cadastro com os erros do formulario atual
		#	return render(request, "Usuario\cadastro.html", {"form": form})

	#se nenhuma informação for passada, exibe a pagina de cadastro
	return render(request, "Usuario\cadastro.html", {"form": UserCreationForm()})






		