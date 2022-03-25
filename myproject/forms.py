from django import forms
from . models import Cakes
class CakeForm(forms.ModelForm):
    class Meta:
        model=Cakes
        fields={'name','desc','price','img'}