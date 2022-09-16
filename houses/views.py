from math import ceil
from http.client import HTTPResponse
from datetime import datetime
from django.shortcuts import render
from . import models


def all_houses(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_houses = models.House.objects.all()[offset:limit]
    page_count = ceil(models.House.objects.count() / page_size)
    return render(
        request,
        "home.html",
        context={
            "houses": all_houses,
            "page": page,
            "page_count": page_count,
            "page_range": range(1, page_count),
        },
    )
