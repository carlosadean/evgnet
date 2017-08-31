# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
# Create your models here.

class Igreja(models.Model):
	nome = models.CharField(max_length=50, default='')
	email = models.EmailField(max_length=50)
	sede_regional = models.BooleanField(default=False)
	sede_bloco = models.BooleanField(default=False)
	#responsavel_evg = models.ForeignKey(Evangelista, blank=True, null=True)

	def __str__(self):
		return self.nome.encode('utf-8')

class Projeto(models.Model):
 	nome = models.CharField(max_length=50)

 	def __str__(self):
		return self.nome.encode('utf-8')
	

class Funcao(models.Model):
 	nome = models.CharField(max_length=50)

 	def __str__(self):
		return self.nome.encode('utf-8')


class Evangelista(models.Model):
	igreja = models.ForeignKey(Igreja)
	projeto = models.ForeignKey(Projeto)
	funcao = models.ForeignKey(Funcao)
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	data_entrada_evg = models.DateField()
	foto_perfil = models.ImageField(upload_to='foto_perfil/',
							blank=True)
	# GENDER_CHOICES = (
 #        ('M', 'Masculino'),
 #        ('F', 'Feminino'),
 #    )
    
 #    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	
	# ESTADO_CIVIL = (
 #        ('S', 'Solteiro'),
 #        ('C', 'Casado'),
 #        ('D', 'Divorciado'),
 #        ('U', 'União Estável'),
 #    )
    
 #    estado_civil = models.CharField(max_length=1, choices=ESTADO_CIVIL)

	def __str__(self):
		return self.nome.encode('utf-8')
	

