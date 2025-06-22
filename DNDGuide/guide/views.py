from django.shortcuts import render
from .models import *
from django.views.generic import View


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'guide/home.html', {})
