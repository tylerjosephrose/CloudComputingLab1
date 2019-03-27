from django.http import JsonResponse
from rest_framework import generics
from Forecast.serializers import *


class HistoricalListApi(generics.ListAPIView):
    """
    Provides a list of all dates for which weather information is available in YYYYMMDD
    """
    queryset = Weather.objects.all()
    serializer_class = HistoricalSerializer

    def post(self, request):
        print(request.data)
        data = request.data

        # Make sure they sent the right data
        date = ""
        try:
            if set(['DATE', 'TMAX', 'TMIN']) == set(data):
                date = data['DATE']
                tmax = round(data['TMAX'], 1)
                tmin = round(data['TMIN'], 1)

                # Make sure the date they sent conforms
                date_check = int(int(date)/10000000)
                if 0 < date_check < 10:
                    # 90.7|68.9|2019-03-27
                    date_input = "{}-{}-{}".format(date[:4], date[4:6], date[6:8])
                    obj, created = Weather.objects.update_or_create(DATE__year=date[:4],
                                                                    DATE__month=date[4:6],
                                                                    DATE__day=date[6:8],
                                                                    defaults={'DATE': date_input,
                                                                              'TMAX': tmax,
                                                                              'TMIN': tmin})
            else:
                return JsonResponse({'error': 'Not the right post body...please use DATE, TMAX, and TMIN with '
                                              'appropriate values'}, status=400)
        except Exception as e:
            print(e)
            return JsonResponse({'error': e}, status=400)
        return JsonResponse({'DATE': date}, status=201)


class HistoricalLookupApi(generics.ListAPIView):
    """
    Provides the Weather for the given date in YYYYMMDD
    """
    queryset = Weather.objects.all()
    serializer_class = HistoricalLookupSerializer

    def delete(self, request, date):
        print(date)

        # This check should be covered by the regex url...but just in case
        if not len(date) == 8:
            return JsonResponse({'error': "Weather at this date was not found"}, status=404)

        try:
            Weather.objects.get(DATE__year=date[:4],
                                DATE__month=date[4:6],
                                DATE__day=date[6:8]).delete()
        except Exception as e:
            return JsonResponse({'error': "Weather at this date was not found"}, status=404)
        return JsonResponse({'DATE': date}, status=200)

    def list(self, request, *args, **kwargs):
        response = super(HistoricalLookupApi, self).list(request, *args, **kwargs)  # call the original 'list'
        try:
            response.data = response.data[0]  # customize the response data
        except:
            return JsonResponse({'error': 'Weather at this date was not found'}, status=404)
        return response  # return response with this custom representation

    def get_queryset(self):
        date = self.request.META['PATH_INFO'].split('/')[3]

        # This check should be covered by the regex url...but just in case
        if not len(date) == 8:
            return

        queryset = Weather.objects.filter(DATE__year=date[:4],
                                          DATE__month=date[4:6],
                                          DATE__day=date[6:8])
        return queryset


class ForecastApi(generics.ListAPIView):
    """
    Provides the Forecast for the given next 7 days starting on date in YYYYMMDD
    """
    #queryset = Weather.objects.all()
    serializer_class = ForecastSerializer

    def list(self, request, *args, **kwargs):
        response = super(ForecastApi, self).list(request, *args, **kwargs)  # call the original 'list'
        try:
            response.data = response.data[0]  # customize the response data
        except:
            return JsonResponse({'error': 'Weather at this date was not found'}, status=404)
        return response  # return response with this custom representation

    def get_queryset(self):
        date = self.request.META['PATH_INFO'].split('/')[3]

        # This check should be covered by the regex url...but just in case
        if not len(date) == 8:
            return

        #queryset = Weather.objects.filter(DATE__year=date[0:4],
        #                                  DATE__month=date[4:6],
        #                                  DATE__day=date[6:8])
        return [datetime.datetime.strptime(date, "%Y%m%d")]
