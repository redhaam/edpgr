# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.base_user import AbstractBaseUser
from djongo import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Candidat(models.Model):
    first_name = models.CharField( max_length=200)
    last_name = models.CharField( max_length=200)
    organization = models.CharField(max_length=50)
    profile_pic = models.ImageField()


    def get_fullname(self):
        return f'{self.first_name} {self.last_name}'



class Dossier(models.Model):    
    TYPES_CHOICES = ()
    STATUS_CHOICES = (('submitted','Non traité'), ('scheduled','programmé'), ('done','traité'))
    type = models.CharField(max_length=50)
    owner = models.ForeignKey(Candidat, on_delete=models.DO_NOTHING, related_name="owner",null=True,blank=True)
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

    def get_absolute_url(self):
        return reverse("document_detail", kwargs={"document_id": self.id})
    


class Proces_verbal(models.Model):#TODO: add status choices
    id = models.ObjectIdField(primary_key=True)
    title = models.CharField(max_length=150)
    link_to = models.URLField()
    date = models.DateTimeField()
    closing_hour = models.TimeField()
    status = models.CharField(max_length=100)
    validated_by = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    updated = models.DateTimeField(auto_now=True)

class Meeting(models.Model):
    _id= models.ObjectIdField('',primary_key= True)
    organizer = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="meeting_organizer")
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    body = models.TextField()
    attached_files = models.URLField()
    # guests = models.ArrayField(model_container = User)
    # folders_to_treat = models.ArrayField(model_container = Dossier)
    pv = models.ForeignKey(Proces_verbal ,on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now=True)
    status = models.CharField("submitted", max_length=50)

class Interest(models.Model):
    value = models.CharField(max_length=50, primary_key= True)
    label = models.CharField(max_length=50)

class Expert(models.Model):
    _id = models.ObjectIdField('',primary_key=True)
    full_name = models.CharField(max_length=50)
    title = models.CharField( max_length=50)
    grade = models.CharField( max_length=50)
    organization = models.CharField(max_length=50)
    #interests = models.ArrayField(model_container = Interest)
    interests = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("expert_detail", kwargs={"pk": self.pk})