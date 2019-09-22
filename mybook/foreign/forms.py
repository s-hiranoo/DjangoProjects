from django import forms
from .models import Dealer, Farmer, FieldOfficer



class SearchForm(forms.Form):
    name = forms.CharField(
        initial='',
        label='Name',
        required = False, # 必須ではない
    )
    product = forms.CharField(
        initial='',
        label='Product',
        required=False,  # 必須ではない
    )
    season = forms.CharField(
        initial='',
        label='Season',
        required=False,  # 必須ではない
    )
    location = forms.CharField(
        initial='',
        label='Location',
        required=False,  # 必須ではない
    )