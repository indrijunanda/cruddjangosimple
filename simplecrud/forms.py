from django import forms

from simplecrud.models import Crudsimple

class CrudsimpleForm(forms.ModelForm):
    class Meta:
        model = Crudsimple
        fields = "__all__"