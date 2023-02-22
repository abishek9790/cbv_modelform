from django import forms
from app.models import *



class jspform(forms.ModelForm):
    class Meta:
        model=jsp
        fields='__all__'
