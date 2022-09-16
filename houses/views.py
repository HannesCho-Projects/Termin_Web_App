from http.client import HTTPResponse
from datetime import datetime
from django.shortcuts import render
from . import models


def all_houses(request):
    all_houses = models.House.objects.all()
    return render(request, "home.html", context={"houses": all_houses})
