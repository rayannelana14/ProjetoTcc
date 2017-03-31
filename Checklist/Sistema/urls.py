from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cadastroSistema/$', views.cadastroSistema, name = 'cadastroSistema'),
]