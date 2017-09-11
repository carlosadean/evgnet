# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Evangelista

def cadastro_create(request):
	return HttpResponse("<h1>Create Cadastro</h1>")


def cadastro_detail(request, id):
	#instance = Evangelista.objects.get(id=8)
	instance = get_object_or_404(Evangelista, id=id)
	context = {
		"instance": instance.nome,
		"title": "Detail"
	}
	return render(request, "detail.html", context)

def cadastro_list(request):
	queryset = Evangelista.objects.all()

	context = {
		"lista_evangelistas": queryset,
		"title": "List"
	}

	# if request.user.is_authenticated():
	# 	context = {
	# 		"title": "My user List"
	# 	}
	# else:
	# 	context = {
	# 		"title": "List"
	# 	}

	return render(request, "index.html", context)
	# return HttpResponse("<h1>List Cadastro</h1>")


def cadastro_update(request):
	return HttpResponse("<h1>Update Cadastro</h1>")


def cadastro_delete(request):
	return HttpResponse("<h1>Delete Cadastro</h1>")