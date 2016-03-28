# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20160227_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skvhistory',
            name='expluatation',
            field=models.CharField(choices=[('BD', 'Бездействующая'), ('NN', 'Нагнетательная'), ('GL', 'Газлифт'), ('SK', 'Станок-Качалка'), ('RF', 'Ротафлекс'), ('L', 'Ликвидированная'), ('LO', 'Ожидающая ликвидации'), ('UCN', 'УЭЦН'), ('CNTR', 'Контрольная'), ('RAZ', 'Разведочная'), ('PAR', 'Параметрическая')], default='BD', max_length=20, verbose_name='Способ эксплуатации'),
        ),
    ]
