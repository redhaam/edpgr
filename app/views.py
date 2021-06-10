# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .models import Dossier, Proces_verbal

@login_required(login_url="/login/")
def index(request):
    
    context = {}
    context['segment'] = 'dashboard'

    dossiers = Dossier.objects.all()
    context['dossiers'] = dossiers

    html_template = loader.get_template( 'dashboard.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def documents_view(request):
    
    context = {}
    context['segment'] = 'documents'

    pvs = Proces_verbal.objects.all()
    print(pvs)
    context['pvs'] = pvs

    html_template = loader.get_template( 'documents.html' )
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def 

#pv = Proces_verbal.objects.all()
#    context['proces_verbal'] = pv

    


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
