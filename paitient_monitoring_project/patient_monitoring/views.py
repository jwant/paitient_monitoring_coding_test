from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'index.html')
