from django.urls import path, include

from .views import ProfileView

urlpatterns = [
    path('', ProfileView.as_view(), name='profiles'),
    path('create_clinician', ProfileView.as_view(profile_create_type='clinician'), name='create_clinician'),
    path('create_patient', ProfileView.as_view(profile_create_type='patient'), name='create_patient'),
]
