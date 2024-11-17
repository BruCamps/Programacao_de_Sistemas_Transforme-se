from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
