# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20160227_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skvconst',
            name='skv_date_expluatation',
            field=models.DateField(verbose_name='Дата создания скважены'),
        ),
    ]