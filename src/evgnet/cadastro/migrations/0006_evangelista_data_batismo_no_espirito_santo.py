# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_remove_evangelista_data_batismo_no_espirito_santo'),
    ]

    operations = [
        migrations.AddField(
            model_name='evangelista',
            name='data_batismo_no_espirito_santo',
            field=models.DateField(null=True),
        ),
    ]
