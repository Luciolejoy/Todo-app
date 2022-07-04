from turtle import title
from django import forms
from django.forms import ModelForm

from .models import *


class AufgabeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'neue Aufgabe hinzufügen'}))

    class Meta:
        model = Aufgabe
        fields = '__all__'
