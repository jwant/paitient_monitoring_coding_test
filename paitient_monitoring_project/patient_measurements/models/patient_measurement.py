from django.db import models

class PatientMeasurement(models.Model):
    date = models.DateField()
    heart_rate = models.FloatField()
    blood_pressure = models.FloatField()
    weight = models.FloatField()
