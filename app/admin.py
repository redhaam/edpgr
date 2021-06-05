# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.models import Dossier, Meeting
from django.contrib import admin

# Register your models here.


@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_filter = ('status',)