from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^categoria/$', views.categoria, name = 'categoria'),
	url(r'^questao/$', views.questao, name = 'questao'),
	url(r'^checklist/$', views.checklist, name = 'checklist'),
	url(r'^checkindex/$', views.checkindex, name = 'checkindex'),
	url(r'^avaliacao/$', views.avaliacao, name = 'avaliacao'),
	url(r'^respCheck/(?P<pk>[0-9]+)/$', views.respCheck, name = 'respCheck'),
	url(r'^avaliacao_list/$', views.avaliacao_list, name = 'avaliacao_list'),
]