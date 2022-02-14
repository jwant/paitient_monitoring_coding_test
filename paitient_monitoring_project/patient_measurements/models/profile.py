from django.db import models
from django.contrib.auth.models import User
from .patient_measurement import PatientMeasurement


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_clinician = models.BooleanField(default=False)
    patient_ids = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_patient_ids')

    is_patient = models.BooleanField(default=False)
    patient_measurements = models.ForeignKey(PatientMeasurement, on_delete=models.SET_NULL, null=True)
