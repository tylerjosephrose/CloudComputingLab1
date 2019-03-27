from django.urls import path, re_path
from Forecast.api.api import HistoricalListApi, HistoricalLookupApi, ForecastApi

app_name = 'api'

urlpatterns = [
    path('historical/', HistoricalListApi.as_view(), name="historical"),
    re_path(r'^historical/(?P<date>\d{4}\d{2}\d{2})$', HistoricalLookupApi.as_view(), name='historicalLookup'),
    re_path(r'^forecast/(?P<date>\d{4}\d{2}\d{2})$', ForecastApi.as_view(), name='forecast'),
]