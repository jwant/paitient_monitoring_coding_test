from django.urls import path, include

from .views import PatientMeasurementsView

urlpatterns = [
    path('', PatientMeasurementsView.as_view(), name='patient_measurements'),
    path('create_measurement', PatientMeasurementsView.as_view(new_measurement=True), name='create_measurement'),
]
