# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='igreja',
            name='sede_estadual',
            field=models.BooleanField(default=False),
        ),
    ]