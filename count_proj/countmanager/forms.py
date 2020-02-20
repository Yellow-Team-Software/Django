from django import forms
from django.forms import ModelForm

from .models import *


class RoomForm(forms.ModelForm):
    #name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
	    model = Room
	    fields = '__all__'

class SessForm(forms.ModelForm):
    #name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
	    model = Session
	    fields = '__all__'

class SpeakerForm(forms.ModelForm):
    #name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
	    model = Speaker
	    fields = '__all__'