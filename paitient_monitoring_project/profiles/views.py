from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import Http404
from .models import Profile

class ProfileView(LoginRequiredMixin, View):
    profile_create_type=""

    def get(self, request):
        clinician_ids = User.objects.filter(profile__is_clinician=True)
        profile = Profile.objects.filter(user_id=request.user.id)
        is_admin = request.user.is_superuser
        is_clinician = profile and profile[0].is_clinician

        if is_admin:
            patient_ids = User.objects.filter(profile__is_patient=True)
        elif is_clinician:
            patient_ids = profile[0].get_patient_ids()
        else:
            patient_ids = []

        context = {
            'clinician_ids': clinician_ids,
            'patient_ids': patient_ids,
            'is_admin': is_admin,
            'is_clinician': is_clinician,
        }
        return render(request, 'profiles.html', context)

    def post(self, request):
        if self.profile_create_type:
            self.new_profile(request, self.profile_create_type)
        return self.get(request)

    def new_profile(self, request, type):
        if not (request.user.is_superuser or request.user.profile.is_clinician and type == 'patient'):
            raise Http404('Your account does not have the correct permissions')

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
            p.clinician_id = request.user
        elif type=='clinician':
            p.is_clinician = True

        # Todo: set clinician -> client relationship

        p.save()
