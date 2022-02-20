from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import PatientMeasurement
from profiles.models.profile import Profile
from datetime import datetime

class PatientMeasurementsView(LoginRequiredMixin, View):
    new_measurement=False

    def get(self, request):
        profile = Profile.objects.filter(user_id=request.user.id)
        is_patient = profile and profile[0].is_patient
        is_clinician = profile and profile[0].is_clinician
        is_admin = request.user.is_superuser

        if is_patient:
            measurement_ids = PatientMeasurement.objects.filter(patient_id=request.user.id)
        elif is_clinician:
            patient_ids = Profile.objects.filter(clinician_id=request.user.id)
            measurement_ids = PatientMeasurement.objects.filter(patient_id__in=[p.user for p in patient_ids])
        else:
            measurement_ids = []
        context = {
            'measurement_ids': measurement_ids,
            'is_clinician': is_clinician,
        }

        return render(request, 'measurements.html', context)

    def post(self, request):
        if self.new_measurement and request.user.profile.is_patient:
            PatientMeasurement.objects.create(
                date=datetime.now(),
                heart_rate=request.POST.get('heart_rate',False),
                blood_pressure=request.POST.get('blood_pressure',False),
                weight=request.POST.get('weight',False),
                patient_id=request.user,
            )

        return self.get(request)
