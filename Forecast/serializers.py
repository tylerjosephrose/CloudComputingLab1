import datetime

from .Forecasting import Forecasting
from rest_framework import serializers
from .models import Weather


class HistoricalSerializer(serializers.ModelSerializer):
    DATE = serializers.DateField(format="%Y%m%d")

    class Meta:
        model = Weather
        fields = ("DATE",)


class HistoricalLookupSerializer(serializers.ModelSerializer):
    DATE = serializers.DateField(format="%Y%m%d")

    class Meta:
        model = Weather
        fields = ("DATE", "TMAX", "TMIN")


class ForecastSerializer(serializers.Serializer):

    def to_representation(self, date):
        f = Forecasting.get_instance()
        forecast_tmax, forecast_tmin = f.get_forecast(date)
        result = []
        for key in forecast_tmax:
            tmax = float("{0:.1f}".format(forecast_tmax[key]))
            tmin = float("{0:.1f}".format(forecast_tmin[key]))
            result.append({"DATE": key.strftime("%Y%m%d"), "TMAX": tmax, "TMIN": tmin})
        return result
