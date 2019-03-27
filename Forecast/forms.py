from django import forms
from django.forms import widgets
import datetime


class ForecastForm(forms.Form):
    date = forms.DateField(initial=datetime.date.today(), widget=widgets.SelectDateWidget(years=range(2000, 2050)))
