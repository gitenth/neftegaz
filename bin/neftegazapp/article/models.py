# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class SkvConst(models.Model):
    class Meta():
        db_table = "skv_const_info"
        verbose_name = u'Скважины'
    skv_name = models.CharField(u'Название скважины', max_length=50)
    skv_date_expluatation = models.DateField(u'Дата создания скважины')
    skv_zaboy = models.FloatField(u'Пробуренный забой')
    skv_altituda = models.FloatField(u'Альтитуда')
    skv_napr_d = models.FloatField(u'Диаметра направления, мм')
    skv_napr_h = models.FloatField(u'Глубина направления, м')
    skv_teh_colonna_d = models.FloatField(u'Диаметр технической колонны, мм')
    skv_teh_colonna_h = models.FloatField(u'Глубина залегания технической колонны, м')
    skv_eksp_colonna_d = models.FloatField(u'Диаметр эксплуатационной колонны, мм', blank=True, null=True)
    skv_eksp_colonna_h = models.FloatField(u'Глубина залегания эксплуатационной колонны, м', blank=True, null=True)
    skv_prod_horizont = models.FloatField(u'Кровля продуктивного горизонта, м', blank=True, null=True)
    skv_angidrit_up_up = models.FloatField(u'Верхний ангидрид, кровля, м', blank=True, null=True)
    skv_angidrit_up_down = models.FloatField(u'Верхний ангидрид, подошва, м', blank=True, null=True)
    skv_angidrit_sr_up = models.FloatField(u'Средний ангидрит, кровля, м', blank=True, null=True)
    skv_angidrit_sr_down = models.FloatField(u'Средний ангидрит, подошва, м', blank=True, null=True)
    skv_angidrit_down_up = models.FloatField(u'Нижний ангидрит, кровля, м', blank=True, null=True)
    skv_angidrit_down_down = models.FloatField(u'Нижний ангидрит, подошва, м', blank=True, null=True)

class SkvHistory(models.Model):
    class Meta():
        db_table = 'history'
        verbose_name = u'История'
    CHOISES_EXPLUATATION = (
        ('', ''),
        ('BD', u'Бездействующая'),
        ('NN', u'Нагнетательная'),
        ('GL', u'Газлифт'),
        ('SK',u'Станок-Качалка'),
        ('RF', u'Ротафлекс'),
        ('L', u'Ликвидированная'),
        ('LO', u'Ожидающая ликвидации'),
        ('UCN', u'УЭЦН'),
        ('CNTR', u'Контрольная'),
        ('RAZ', u'Разведочная'),
        ('FND', u'Поисковая'),
        ('PAR', u'Параметрическая'),
    )
    date_work = models.DateField(u'Дата проведения работ', default=None)
    history = models.TextField(u'Описание проведенных работ')
    perforation_up = models.FloatField(u'Верхнее значение перфорации', blank=True, null=True)
    perforation_down = models.FloatField(u'Нижнее значение перфорации', blank=True, null=True)
    expluatation = models.CharField(u'Способ эксплуатации', choices=CHOISES_EXPLUATATION, max_length=20)
    id_skv = models.ForeignKey(SkvConst)

class Dobicha(models.Model):
    class Meta():
        db_table = 'dobicha'
        verbose_name = u'Добыча'

    dobicha_date = models.DateField(u'Дата замера')
    q_water = models.FloatField(u'Дебит по воде, м3/сут')
#    obvodn = models.FloatField(u'Обводненность %')
    q_neft = models.FloatField(u'Дебит по нефти, т/сут')
    q_key = models.ForeignKey(SkvConst)


