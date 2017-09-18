# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import EvangelistaForm
from .models import Evangelista

def cadastro_create(request):
	form = EvangelistaForm(request.POST or None) #esse parametro habilita a validacao no form
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#message success
		messages.success(request, "Cadastro realizado com sucesso!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

def cadastro_detail(request, id):
	instance = get_object_or_404(Evangelista, id=id)
	context = {
		"instance": instance,
		"title": "Detail"
	}
	return render(request, "detail.html", context)

def cadastro_list(request):
	queryset = Evangelista.objects.all()

	context = {
		"lista_evangelistas": queryset,
		"title": "List"
	}

	return render(request, "base.html", context)

def cadastro_update(request, id):
	instance = get_object_or_404(Evangelista, id=id)
	form = EvangelistaForm(request.POST or None, instance=instance) #esse parametro habilita a validacao no form
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		#message success
		messages.success(request, "Cadastro atualizado com sucesso!")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"nome": instance.nome,
		"instance": instance,
		"form": form,
	}
	return render(request, "post_form.html", context)

def cadastro_delete(request, id=None):
	instance = get_object_or_404(Evangelista, id=id)
	instance.delete()
	messages.success(request, "Cadastro removido com sucesso!")
	return redirect("cadastro:lista")
	#return HttpResponse("<h1>Delete Cadastro</h1>")