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
    path('documents/<int:document_id>', views.dossier_detail_view, name='document_detail'),
    path('proces_verbal/<int:pv_id>', views.pv_detail_view, name='pv_detail'),
    path('during_meetings/<int:meeting_id>', views.during_meeting_view, name='during_meeting'),
    


    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
