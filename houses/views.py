from http.client import HTTPResponse
from datetime import datetime
from django.shortcuts import render


def all_houses(request):
    now = datetime.now()
    hungry = True
    return render(request, "all_houses.html", context={"now": now, "hungry": hungry})
