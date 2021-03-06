# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Igreja(models.Model):
	nome = models.CharField(max_length=50, default='')
	email = models.EmailField(max_length=50)
	sede_regional = models.BooleanField(default=False)
	sede_bloco = models.BooleanField(default=False)
	sede_estadual = models.BooleanField(default=False)
	#responsavel_evg = models.ForeignKey(Evangelista, blank=True, null=True)


	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome.encode('utf-8')

class Projeto(models.Model):
 	nome = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nome

 	def __str__(self):
		return self.nome.encode('utf-8')
	

class Funcao(models.Model):
 	nome = models.CharField(max_length=50)

	def __unicode__(self):
		return self.nome

 	def __str__(self):
		return self.nome.encode('utf-8')

def upload_location(instance, filename):
	filebase, extension = filename.split(".")
	return "%s/%s.%s" %(instance.id, instance.id, extension)

class Evangelista(models.Model):
	igreja = models.ForeignKey(Igreja)
	projeto = models.ForeignKey(Projeto)
	funcao = models.ForeignKey(Funcao)
	nome = models.CharField(max_length=200)
	data_nascimento = models.DateField()
	data_entrada_evg = models.DateField()
	foto_perfil = models.ImageField(upload_to=upload_location,
			null=True, 
			blank=True, 
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	data_batismo_no_espirito_santo = models.DateField(null=True)
	obreiro = models.BooleanField(default=False)
	inativo = models.BooleanField(default=False)

	def __unicode__(self):
		return self.nome

	def __str__(self):
		return self.nome.encode('utf-8')

	def get_absolute_url(self):
		return reverse("cadastro:detail", kwargs={"id": self.id})
		#return "/cadastro/%s/" % (self.id)

	def get_edit_url(self):
		return "/cadastro/%s/edit" % (self.id)

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

