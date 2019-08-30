from django import forms
from .models import Member


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('reserve_time',)

