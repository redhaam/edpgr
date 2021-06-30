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
    path('documents/<int:document_id>', views.dossier_detail_view, name='document_detail'),
    path('proces_verbal/<int:pv_id>', views.pv_detail_view, name='pv_detail'),
    path('meetings', views.meetings_view, name='meetings'),
    path('members', views.members_view, name='members'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
