# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20160227_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dobicha',
            name='dobicha_date',
            field=models.DateField(verbose_name='Дата замера'),
        ),
    ]