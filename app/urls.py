# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('dashboard.html', views.dashboard_view),
    path('documents.html', views.documents_view, name='documents'),
    path('documents.html/<int:document_id>', views.document_detail_view, name='document_detail'),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
