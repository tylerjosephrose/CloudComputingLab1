import requests
from django.conf import settings
from django.shortcuts import render, reverse
from django.views.generic import TemplateView

import datetime
import pyowm

from Forecast.forms import ForecastForm


class Forecast(TemplateView):

    def get(self, request):
        form = ForecastForm()
        url = '/table/'
        return render(request, 'Forecast/index.html', {'form': form, 'table_url': url})


class Table(TemplateView):
    def __init__(self):
        self.owm = pyowm.OWM(settings.OPENWEATHERMAP_API_KEY)

    def get_owm_weather(self):
        weathers = self.owm.three_hours_forecast_at_id(settings.OPENWEATHERMAP_CINCY_ID).get_forecast().get_weathers()
        owm_tmax = {}
        owm_tmin = {}
        for entry in weathers:
            date = entry.get_reference_time('date').strftime('%B %d, %Y')
            if owm_tmax.get(date) is None or owm_tmax.get(date) < entry.get_temperature('fahrenheit')['temp_max']:
                owm_tmax[date] = entry.get_temperature('fahrenheit')['temp_max']
            if owm_tmin.get(date) is None or owm_tmin.get(date) > entry.get_temperature('fahrenheit')['temp_min']:
                owm_tmin[date] = entry.get_temperature('fahrenheit')['temp_min']

        return list(owm_tmax.keys()), [str(s) + ' ℉' for s in list(owm_tmax.values())], \
               [str(s) + ' ℉' for s in list(owm_tmin.values())]

    def get(self, request, date):
        internal = requests.get(settings.URL + reverse('api:forecast', kwargs={'date': date}))

        if internal.status_code == 200:
            internal_json = internal.json()
            my_headers = []
            my_tmax = []
            my_tmin = []
            owm_headers = []
            owm_tmax = []
            owm_tmin = []
            for entry in internal_json:
                my_headers.append(datetime.datetime.strptime(entry['DATE'], '%Y%m%d').strftime('%B %d, %Y'))
                my_tmax.append(str(entry['TMAX']) + ' ℉')
                my_tmin.append(str(entry['TMIN']) + ' ℉')

            if datetime.datetime.strptime(date, "%Y%m%d").date() == datetime.datetime.today().date():
                owm_headers, owm_tmax, owm_tmin = self.get_owm_weather()
            return render(request, 'Forecast/table.html', {'my_headers': my_headers, 'tmax': my_tmax,
                                                           'tmin': my_tmin, 'owm_headers': owm_headers,
                                                           'owm_tmax': owm_tmax, 'owm_tmin': owm_tmin})
