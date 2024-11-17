from django.urls import path
from . import views

urlpatterns = [
    path('novo/', views.cadastrar_pessoa, name='cadastrar_pessoa'),
    path('resposta/', views.resposta, name='resposta'),
    path('cadastrados/', views.listar_pessoas, name='listar_pessoas'),
]