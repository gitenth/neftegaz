#-*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from article.models import SkvConst, SkvHistory, Dobicha
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from forms import AddSkv

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
        'username': auth.get_user(request).username,
        'active': 1,
    })

@login_required(login_url='/auth/login/')
def add(request):
    return render_to_response('add.html', {
        'expluatation_method': CHOISES_EXPLUATATION,
        'username': auth.get_user(request).username,
        'active': 2,
    })

@login_required(login_url='/auth/login/')
def new(request):
    if request.method == 'POST':
        form = AddSkv(request.POST)
        if form.is_valid():
            post = form.save()
            return HttpResponseRedirect('/new/')
    else:
        form = AddSkv()
    return render(request, 'new.html', {
        'form': form,
        'username': auth.get_user(request).username,
        'active': 2,
    })