from django import forms
from django.forms import widgets
from .models import User

guest_choices = list(User.objects.all())
guest_choices= list(map(lambda guest: guest.username,guest_choices))

class MeetingForm(forms.Form):
    meeting_title= forms.CharField(label="Titre de la réunion",required=True)
    meeting_body = forms.CharField(empty_value="Description",help_text="Description", widget=widgets.Textarea)
    meeting_date =forms.DateTimeField(label="Date et heure de la réunion :",required=True)
    guests = forms.TypedChoiceField(required=True)
    # folders_to_treat = forms.CheckboxInput(attrs=[])
