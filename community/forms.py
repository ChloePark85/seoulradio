from django.forms import ModelForm
from community.models import *

class Form(ModelForm):
    class Meta:
        model=Article
        fields=['name','place','title','contents','tag']