from django.db import models
from django.contrib.auth.models import User

class PatientMeasurement(models.Model):
    date = models.DateTimeField()
    heart_rate = models.FloatField()
    blood_pressure = models.FloatField()
    weight = models.FloatField()
    patient_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

