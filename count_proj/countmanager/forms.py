from django import forms
from django.forms import ModelForm, ModelChoiceField, ModelMultipleChoiceField

from .models import *


class CountsForm(forms.ModelForm):
    #name= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta:
	    model = Counts
	    fields = '__all__'

