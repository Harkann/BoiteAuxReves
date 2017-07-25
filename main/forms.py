from django import forms
from .models import Reve

class ReveForm(forms.ModelForm):

        class Meta:
            model = Reve
            fields = ("auteur","titre","contenu")
