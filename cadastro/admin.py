# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Igreja, Projeto, Funcao, Evangelista
# Register your models here.

class EvangelistaModelAdmin(admin.ModelAdmin):
	list_display = ["nome", "data_nascimento", "data_entrada_evg"]
	list_filter = ["data_nascimento", "data_entrada_evg"]

# admin.site.register(Igreja)
# admin.site.register(Projeto)
# admin.site.register(Funcao)
admin.site.register(Evangelista, EvangelistaModelAdmin)