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
from .MeetingForm import MeetingForm

@login_required(login_url="/login/")
def index(request):
    return dashboard_view(request)


@login_required(login_url="/login/")
def dashboard_view(request):
    
    context = {}
    context['segment'] = 'dashboard'

    dossiers = Dossier.objects.all()
    nb_folders_to_be_treated = len(dossiers.filter(status="scheduled"))
    nb_folders = len(dossiers)
    context['dossiers'] = dossiers
    context['nb_folders'] = nb_folders
    context['to_be_treated'] =nb_folders_to_be_treated
    html_template = loader.get_template( 'dashboard.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def documents_view(request):
    
    context = {}
    context['segment'] = 'documents'

    pvs = Proces_verbal.objects.all()
    context['pvs'] = pvs

    html_template = loader.get_template( 'documents.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url='/login/')
def dossier_detail_view(request,document_id):
    dossier = get_object_or_404(Dossier, id=document_id )

    html_template = loader.get_template('dossier_detail.html')
    return HttpResponse(html_template.render({'dossier' : dossier},request))



@login_required(login_url='/login/')
def pv_detail_view(request,document_id):
    document = get_object_or_404(Proces_verbal, id=document_id )

    html_template = loader.get_template('documents_detail.html')
    return HttpResponse(html_template.render({'document' : document},request))


@login_required(login_url="/login/")
def meetings_view(request):
    html_template = loader.get_template('meetings.html')
    form = MeetingForm()
    return HttpResponse(html_template.render({'segment' : "meetings","scheduleMeeting":form},request)) 


@login_required(login_url="/login/")
def members_view(request):
    html_template = loader.get_template('members.html')
    return HttpResponse(html_template.render({'segment' : "members"},request)) 
    


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
