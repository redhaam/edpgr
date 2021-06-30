from django import forms
from django.forms import ModelForm

from .models import Expert, Meeting

class ExpertPostForm(ModelForm):
    # full_name = forms.CharField(max_length=50)
    # title = forms.CharField( max_length=50)
    # grade = forms.CharField( max_length=50)
    # organization = forms.CharField(max_length=50)
    # #interests = forms.ArrayField(model_container = Interest)
    # interests = forms.CharField(max_length=50)
    class Meta:
        model = Expert
        fields = "__all__"
        # ('full_name', 'title', 'grade', 'organization', 'interests')

class MeetingDuring(ModelForm):
    
    class Meta:
        model = Meeting
        fields = "__all__"