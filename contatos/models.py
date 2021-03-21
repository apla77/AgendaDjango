from django.db import models
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome')
    sobrenome = models.CharField(max_length=255, blank=True, verbose_name='Sobrenome')
    telefone = models.CharField(max_length=255, verbose_name='Telefone')
    email = models.CharField(max_length=255, blank=True, verbose_name='E-Mail')
    data_criacao = models.DateTimeField(default=timezone.now, verbose_name='Data de criação')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, verbose_name='Categoria')
    mostrar = models.BooleanField(default=True, verbose_name='Mostrar')
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/')

    def __str__(self):
        return self.nome





