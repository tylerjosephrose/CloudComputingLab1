from django.db import models


# Create your models here.
class Weather(models.Model):
    DATE = models.DateField(primary_key=True)
    TMAX = models.FloatField()
    TMIN = models.FloatField()

    def __str__(self):
        return "{}: {} - {}".format(self.DATE, self.TMAX, self.TMIN)
