# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.models import Candidat, Dossier, Expert, Meeting, Proces_verbal

from django.contrib import admin

# Register your models here.


@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    
@admin.register(Meeting)
class MeetingAdmin(admin.ModelAdmin):
    list_filter = ('status',)

@admin.register(Proces_verbal)
class DossierAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    
    
@admin.register(Candidat)
class DossierAdmin(admin.ModelAdmin):
    search_fields= ("first_name",)

@admin.register(Expert)
class DossierAdmin(admin.ModelAdmin):
    search_fields= ('full_name',)