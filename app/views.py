# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from .forms import ExpertPostForm, MeetingDuring
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .MeetingForm import MeetingForm
from .models import Dossier, Expert, Proces_verbal

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

@login_required(login_url="/login/")
def experts_view(request):
    
    context = {}
    context['segment'] = 'experts'

    experts = Expert.objects.all()
    context['experts'] = experts

    html_template = loader.get_template( 'experts.html' )
    return HttpResponse(html_template.render(context, request))


@login_required(login_url='/login/')
def dossier_detail_view(request,document_id):
    dossier = get_object_or_404(Dossier, id=document_id )

    html_template = loader.get_template('dossier_detail.html')
    return HttpResponse(html_template.render({'dossier' : dossier},request))



@login_required(login_url='/login/')
def pv_detail_view(request,pv_id):
    document = get_object_or_404(Proces_verbal, id=pv_id )


    html_template = loader.get_template('documents_detail.html')
    return HttpResponse(html_template.render({'document' : document},request))


@login_required(login_url="/login/")
def meetings_view(request):
    html_template = loader.get_template('meetings.html')
    form = MeetingForm()
    return HttpResponse(html_template.render({'segment' : "meetings","scheduleMeeting":form},request)) 

@login_required(login_url='/login/')
def add_expert_view(request):
    #post = get_object_or_404(Expert, slug=post_id)
    # form = ExpertPostForm()

    new_expert = None
    expert_form = ExpertPostForm()

    if request.method == 'POST':
        expert_form = ExpertPostForm(request.POST)
        if expert_form.is_valid():
            new_expert = expert_form.save(commit=False)
            new_expert.save()
            return redirect('experts')
        else:
            expert_form = ExpertPostForm()
    # return render(request, 'add_experts.html', {'form': form})
    html_template = loader.get_template('add_experts.html')
    return  HttpResponse(html_template.render({'new_expert': new_expert, 'expert_form': expert_form},request))#render(request, 'add_experts.html', {'post': post,'experts': experts, 'new_expert': new_expert, 'expert_form': expert_form})

@login_required(login_url='/login/')
def during_meeting_view(request, meetingId):
    post = get_object_or_404(Expert, id=meetingId)
    # form = ExpertPostForm()
    # TODO: continue meeting
    new_meeting = None
    meeting_form = MeetingDuring()

    if request.method == 'POST':
        meeting_during = MeetingDuring(request.POST)
        if meeting_during.is_valid():
            new_meeting = meeting_during.save(commit=False)
            new_meeting.save()
            return redirect('experts')
        else:
            meeting_during = MeetingDuring()
    # return render(request, 'add_experts.html', {'form': form})
    html_template = loader.get_template('durnig_meetings.html')
    return  HttpResponse(html_template.render({'new_meeting': new_meeting, 'meeting_form': meeting_form},request))#render(request, 'add_experts.html', {'post': post,'experts': experts, 'new_expert': new_expert, 'expert_form': expert_form})


# @login_required(login_url="/login/")
# def 


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
