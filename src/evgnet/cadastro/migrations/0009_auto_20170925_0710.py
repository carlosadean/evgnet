# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-25 10:10
from __future__ import unicode_literals

import cadastro.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20170925_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evangelista',
            name='foto_perfil',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=cadastro.models.upload_location, width_field='width_field'),
        ),
    ]
