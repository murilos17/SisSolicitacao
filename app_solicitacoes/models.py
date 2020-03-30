from django.contrib.auth.models import User
from django.db import models

class Usuario(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)
	email = models.EmailField('E-mail', blank=True, null=True)
	

	class Meta:
		verbose_name='Usuario'
		verbose_name_plural='Usuarios'

	def __str__(self):
		return self.nome

class Departamento(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)
	responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)

	class Meta:
		verbose_name='Departamento'
		verbose_name_plural='Departamentos'

	def __str__(self):
		return self.nome

class Automovel(models.Model):
	nome = models.CharField('Nome', max_length=128, blank=True, null=True)

	class Meta:
		verbose_name='Automóvel'
		verbose_name_plural='Automóveis'

	def __str__(self):
		return self.nome

class Solicitar(models.Model):
	Solicitante = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	data = models.DateField(blank=True, null=True)
	horario = models.TimeField(blank=True, null=True)
	origem = models.CharField('Origem', max_length=128, blank=True, null=True)
	destino = models.CharField('Destino', max_length=128, blank=True, null=True)

	class Meta:
		verbose_name='Solicitar Automóvel'
		verbose_name_plural='Solicitar Automóveis'

	def __str__(self):
		return self.destino

class AtenderSolicitacao(models.Model):
	Solicitante = models.ForeignKey(Solicitar, on_delete=models.CASCADE)
	automovel = models.ForeignKey(Automovel, on_delete=models.CASCADE)
	Motorista = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	

	class Meta:
		verbose_name='Atender Solicitação'
		verbose_name_plural='Atender Solicitações'

