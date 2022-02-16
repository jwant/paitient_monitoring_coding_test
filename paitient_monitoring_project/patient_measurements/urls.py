from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_clinician', views.create_clinician, name='create_clinician'),
    path('', include('django.contrib.auth.urls')),  # new
]