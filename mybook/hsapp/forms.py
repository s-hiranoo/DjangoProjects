from .models import Farmer, Dealer
from django import forms

class FarmerCreationForm(forms.ModelForm):

    class Meta:
        model = Farmer
        exclude = ()
        static_id_picture = forms.FileField(
            required=False,
        )
