from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profiles', views.profiles, name='profiles'),
    path('create_clinician', views.create_clinician, name='create_clinician'),
    path('create_patient', views.create_patient, name='create_patient'),
    path('', include('django.contrib.auth.urls')),  # new
]
