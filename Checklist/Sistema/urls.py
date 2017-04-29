from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastroSistema/$', views.cadastroSistema, name = 'cadastroSistema'),
    url(r'^sistema_list/$', views.sistema_list, name = 'sistema_list'),
]