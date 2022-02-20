from django.db import models
from django.contrib.auth.models import User
from patient_measurements.models.patient_measurement import PatientMeasurement


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    is_clinician = models.BooleanField(default=False)

    is_patient = models.BooleanField(default=False)
    clinician_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='user_clinician_id')
    patient_measurements = models.ForeignKey(PatientMeasurement, on_delete=models.SET_NULL, null=True)

    def get_patient_ids(self):
        if self.is_clinician:
            return User.objects.filter(profile__clinician_id=self.user)
        else:
            return False


