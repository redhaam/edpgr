# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from datetime import date
from djongo import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Dossier(models.Model):
    TYPES_CHOICES = ()
    STATUS_CHOICES = (('submitted','Non traité'), ('scheduled','programmé'), ('done','traité'))
    # _id = models.
    type = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="owner",null=True,blank=True)
    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name="sender")
    title = models.CharField(max_length=250)
    attached_files = models.URLField(null=True,blank=True)
    sent_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.TimeField(null=True,blank=True)
    updated = models.TimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    decision= models.CharField(max_length=250,null=True,blank=True)
    remarks = models.CharField(max_length=250,null=True,blank=True)

    class Meta:
        ordering =('-sent_date',)

    def __str__(self):
        return self.title


class Proces_verbal(models.Model):
    title = models.CharField(max_length=150)
    link_to = models.URLField()
    date = models.DateTimeField()
    closing_hour = models.TimeField()
    status = models.CharField(max_length=100)
    validated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)

class Meeting(models.Model):

    organizer = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="meeting_organizer")
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    body = models.TextField()
    attached_files = models.URLField()
    guests = models.ForeignKey(User, on_delete=models.CASCADE,related_name="guests_list")
    folders_to_treat = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    pv = models.ForeignKey(Proces_verbal ,on_delete=models.DO_NOTHING)
    created = models.TimeField(default=timezone.now)
    status = models.CharField(max_length=50)



