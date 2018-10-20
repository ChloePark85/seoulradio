from django import forms
from django.forms import ModelForm
from community.models import *

class Form(forms.ModelForm):
    class Meta:
        model=Articlefields=['name', 'place', 'title', 'contents', 'tag','cdate']
        fields='__all__'