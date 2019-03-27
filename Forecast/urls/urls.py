from django.urls import path, include, re_path
from Forecast.views import Forecast, Table

urlpatterns = [
    path('api/', include('Forecast.urls.api_urls', namespace='api')),
    path('forecast', Forecast.as_view(), name='forecast'),
    re_path(r'^table/(?P<date>\d{4}\d{2}\d{2})$', Table.as_view(), name='forecast'),
]
