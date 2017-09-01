# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def cadastro_create(request):
	return HttpResponse("<h1>Create Cadastro</h1>")


def cadastro_detail(request):
	return HttpResponse("<h1>Detail Cadastro</h1>")


def cadastro_list(request):
	return HttpResponse("<h1>List Cadastro</h1>")


def cadastro_update(request):
	return HttpResponse("<h1>Update Cadastro</h1>")


def cadastro_delete(request):
	return HttpResponse("<h1>Delete Cadastro</h1>")