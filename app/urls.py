# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('dashboard', views.dashboard_view),
    path('documents', views.documents_view, name='documents'),
    path('experts', views.experts_view, name='experts'),
    path('add_experts.html', views.add_expert_view, name='add_experts'),
    path('documents/<document_id>', views.dossier_detail_view, name='document_detail'),
    path('proces_verbal/<pv_id>', views.pv_detail_view, name='pv_detail'),
    path('proces_verbal/<pv_id>/doc', views.pv_doc_view, name='pv_doc'),
    path('meetings', views.meetings_view, name='meetings'),
    path('scheduleMeeting', views.meetings_view, name='meetings'),
    path('members', views.members_view, name='members'),
    path('during_meetings/<meeting_id>', views.during_meeting_view, name='during_meeting'),
    path('settings.html', views.pages,name="pages")


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
