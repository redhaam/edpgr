from django import forms
from django.forms import  widgets
from .models import Dossier, Meeting, Member, User

def get_guest_choices():
    guest_choices = list(Member.objects.all())
    get_value = lambda guest : (guest.id,guest.get_fullname())
    key_value_guests = list(map(get_value,guest_choices))
    print(key_value_guests)
    return(key_value_guests)
    
    
def get_folders_to_treat():
    folders_to_treat = list(Dossier.objects.all().filter(status="submitted"))
    get_value = lambda folder : (folder.id,folder.title)
    return list(map(get_value,folders_to_treat))


class MeetingForm(forms.ModelForm):
    title= forms.CharField(label="Titre de la réunion",required=True)
    date =forms.DateTimeField(label="Date et heure de la réunion :",required=True,widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M'))
    guests = forms.MultipleChoiceField(widget=widgets.CheckboxSelectMultiple,choices=get_guest_choices())
    folders_to_treat = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=get_folders_to_treat())
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model=Meeting
        fields=('title','date','body','guests','folders_to_treat',)
