from django.shortcuts import render
from django.http import HttpResponse
from .models import Pessoa

# Create your views here.
def cadastrar_pessoa(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        data_nascimento = request.POST.get('data_nascimento')

        pessoa = Pessoa(nome=nome, email=email, telefone=telefone, data_nascimento=data_nascimento)
        pessoa.save()

        return render(request, 'cadastro/resposta.html', {'pessoas': pessoa})
    else:
        return render(request, 'cadastro/cadastrar_pessoa.html')

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'cadastro/listar_pessoas.html', {'pessoas': pessoas })
    # Reseta os registros da Tabela Pessoa ->  Pessoa.objects.all().delete()

def resposta(request):
    pessoa = Pessoa.objects.last()
    return render(request, 'cadastro/resposta.html', {'pessoas': pessoa})