from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from article.models import SkvConst, SkvHistory, Dobicha
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
CHOISES_EXPLUATATION = (
        {'DB': u'Добывающая'},
        {'BD': u'Бездействующая'},
        {'NN': u'Нагнетательная'},
        {'L': u'Ликвидированная'},
        {'LO': u'Ожидающая ликвидации'},
        {'CNTR': u'Контрольная'},
        {'RAZ': u'Разведочная'},
        {'FND': u'Поисковая'},
        {'PAR': u'Параметрическая'})

@login_required(login_url='/auth/login/')
def add_zamer(request):
    return render_to_response('addzamer.html', {
        'expluatation_method': CHOISES_EXPLUATATION,
        'username': auth.get_user(request).username,
        'articles': 'slovo',
    } )

@login_required(login_url='/auth/login/')
def articles(request):
    return render_to_response('main.html', {
        'username': auth.get_user(request).username
    })

@login_required(login_url='/auth/login/')
def add(request):
    return render_to_response('add.html', {
        'expluatation_method': CHOISES_EXPLUATATION,
        'username': auth.get_user(request).username
    })
