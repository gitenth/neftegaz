# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_auto_20160227_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dobicha',
            options={'verbose_name': 'Добыча'},
        ),
        migrations.AlterModelOptions(
            name='skvhistory',
            options={'verbose_name': 'История'},
        ),
        migrations.AlterField(
            model_name='skvconst',
            name='skv_angidrit_down_down',
            field=models.FloatField(blank=True, null=True, verbose_name='Нижний ангидрит, подошва, м'),
        ),
        migrations.AlterField(
            model_name='skvconst',
            name='skv_angidrit_down_up',
            field=models.FloatField(blank=True, null=True, verbose_name='Нижний ангидрит, кровля, м'),
        ),
        migrations.AlterField(
            model_name='skvconst',
            name='skv_angidrit_sr_down',
            field=models.FloatField(blank=True, null=True, verbose_name='Средний ангидрит, подошва, м'),
        ),
        migrations.AlterField(
            model_name='skvconst',
            name='skv_angidrit_sr_up',
            field=models.FloatField(blank=True, null=True, verbose_name='Средний ангидрит, кровля, м'),
        ),
        migrations.AlterField(
            model_name='skvconst',
            name='skv_angidrit_up_down',
            field=models.FloatField(blank=True, null=True, verbose_name='Верхний ангидрид, подошва, м'),
        ),
        migrations.AlterField(
            model_name='skvconst',
            name='skv_angidrit_up_up',
            field=models.FloatField(blank=True, null=True, verbose_name='Верхний ангидрид, кровля, м'),
        ),
        migrations.AlterField(
            model_name='skvhistory',
            name='expluatation',
            field=models.CharField(choices=[('', ''), ('BD', 'Бездействующая'), ('NN', 'Нагнетательная'), ('GL', 'Газлифт'), ('SK', 'Станок-Качалка'), ('RF', 'Ротафлекс'), ('L', 'Ликвидированная'), ('LO', 'Ожидающая ликвидации'), ('UCN', 'УЭЦН'), ('CNTR', 'Контрольная'), ('RAZ', 'Разведочная'), ('FND', 'Поисковая'), ('PAR', 'Параметрическая')], max_length=20, verbose_name='Способ эксплуатации'),
        ),
    ]
