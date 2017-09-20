# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
from .forms import EvangelistaForm
from .models import Evangelista

def cadastro_create(request):
    form = EvangelistaForm(request.POST or None, request.FILES or None) #esse parametro habilita a validacao no form
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
    queryset_list = Evangelista.objects.all()
    paginator = Paginator(queryset_list, 10) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)

    context = {
        "lista_evangelistas": queryset,
        "title": "List"
    }

    return render(request, "base.html", context)

def cadastro_update(request, id):
    instance = get_object_or_404(Evangelista, id=id)
    form = EvangelistaForm(request.POST or None, request.FILES or None, instance=instance) #esse parametro habilita a validacao no form
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