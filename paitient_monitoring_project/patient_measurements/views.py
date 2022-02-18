from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Profile


def index(request):
    return render(request, 'index.html')

def profiles(request):
    clinician_ids = User.objects.filter(profile__is_clinician=True)
    patient_ids = User.objects.filter(profile__is_patient=True)
    context = {
        'clinician_ids': clinician_ids,
        'patient_ids': patient_ids,
    }
    return render(request, 'profiles.html', context)

def create_clinician(request):
    new_profile(request, 'clinician')
    return profiles(request)

def create_patient(request):
    new_profile(request, 'patient')
    return profiles(request)

def new_profile(request, type):
    u = User.objects.create_user(
        first_name=request.POST.get('first_name', False),
        last_name=request.POST.get('last_name', False),
        username=request.POST.get('username', False),
        email=request.POST.get('email', False),
        password=request.POST.get('password', False),
    )
    u.save()

    p = Profile.objects.create(user_id=u.id,)
    if type=='patient':
        p.is_patient = True
    elif type=='clincian':
        p.is_clinician = True
    p.save()
