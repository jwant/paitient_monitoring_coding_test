from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .models import Profile

class ProfileView(LoginRequiredMixin, View):
    profile_create_type=""

    def get(self, request):
        clinician_ids = User.objects.filter(profile__is_clinician=True)
        patient_ids = User.objects.filter(profile__is_patient=True)
        context = {
            'clinician_ids': clinician_ids,
            'patient_ids': patient_ids,
        }
        return render(request, 'profiles.html', context)

    def post(self, request):
        if self.profile_create_type:
            self.new_profile(request, self.profile_create_type)
        return self.get(request)

    def new_profile(self, request, type):
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
        elif type=='clinician':
            p.is_clinician = True

        # Todo: check user has the correct profile to run action
        # Todo: set clinician -> client relationship

        p.save()
