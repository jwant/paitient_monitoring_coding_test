from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render

from .models import Profile


def index(request):
    clinician_ids = User.objects.filter(profile__is_clinician=True)
    context = {
        'clinician_ids': clinician_ids,
    }
    return render(request, 'index.html', context)

def create_clinician(request):
    # user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    u = User.objects.create_user(
        first_name=request.POST.get('first_name', False),
        last_name=request.POST.get('last_name', False),
        username=request.POST.get('username', False),
        email=request.POST.get('email', False),
        password=request.POST.get('password', False),
    )
    u.save()
    p = Profile.objects.create(
        user_id=u.id,
        is_clinician=True,
    )
    p.save()

    clinician_ids = User.objects.filter(profile__is_clinician=True)
    context = {
        'clinician_ids': clinician_ids,
    }

    return render(request, 'index.html',context)
