#-*- coding: utf-8 -*-
from django import forms
from models import SkvConst


class AddSkv(forms.Form):
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
    skv_name = forms.CharField(label=u'Название скважины', max_length=50)
    skv_date_expluatation = forms.DateField(label=u'Дата создания скважины')
    skv_zaboy = forms.FloatField(label=u'Пробуренный забой')
    skv_altituda = forms.FloatField(label=u'Альтитуда')
    skv_napr_d = forms.FloatField(label=u'Диаметра направления, мм')
    skv_napr_h = forms.FloatField(label=u'Глубина направления, м')
    skv_teh_colonna_d = forms.FloatField(label=u'Диаметр технической колонны, мм')
    skv_teh_colonna_h = forms.FloatField(label=u'Глубина залегания технической колонны, м')
    skv_eksp_colonna_d = forms.FloatField(label=u'Диаметр эксплуатационной колонны, мм')
    skv_eksp_colonna_h = forms.FloatField(label=u'Глубина залегания эксплуатационной колонны, м')
    skv_prod_horizont = forms.FloatField(label=u'Кровля продуктивного горизонта, м')
    skv_angidrit_up_up = forms.FloatField(label=u'Верхний ангидрид, кровля, м')
    skv_angidrit_up_down = forms.FloatField(label=u'Верхний ангидрид, подошва, м')
    skv_angidrit_sr_up = forms.FloatField(label=u'Средний ангидрит, кровля, м')
    skv_angidrit_sr_down = forms.FloatField(label=u'Средний ангидрит, подошва, м')
    skv_angidrit_down_up = forms.FloatField(label=u'Нижний ангидрит, кровля, м')
    skv_angidrit_down_down = forms.FloatField(label=u'Нижний ангидрит, подошва, м')
    expluatation = forms.ChoiceField(label=u'Способ эксплуатации', choices=CHOISES_EXPLUATATION)
    def save(self):
        post = SkvConst(**self.cleaned_data)
        post.save()
        return post
