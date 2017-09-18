from django.conf.urls import url
from django.contrib import admin

from .views import (
	cadastro_list,
	cadastro_create,
	cadastro_detail,
	cadastro_update,
	cadastro_delete,
	)

urlpatterns = [
	url(r'^$', cadastro_list, name='lista'),
	url(r'^create/$', cadastro_create),
	url(r'^(?P<id>\d+)/$', cadastro_detail, name="detail"),
	url(r'^(?P<id>\d+)/edit/$', cadastro_update, name="update"),
	url(r'^(?P<id>\d+)/delete/$', cadastro_delete),
	url(r'^imagens/$', cadastro_delete),
]

"""
urlpatterns = [
	url(r'^$', "posts.views.posts_list"),
    url(r'^create/$', "posts.views.posts_create"),
    url(r'^detail/$', "posts.views.posts_detail"),
    url(r'^update/$', "posts.views.posts_update"),
    url(r'^delete/$', "posts.views.posts_delete"),
]

"""