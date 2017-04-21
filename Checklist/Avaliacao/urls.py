from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^categoria/$', views.categoria, name = 'categoria'),
	url(r'^questao/$', views.questao, name = 'questao'),
	url(r'^checklist/$', views.checklist, name = 'checklist'),
	url(r'^checkindex/$', views.checkindex, name = 'checkindex'),
]