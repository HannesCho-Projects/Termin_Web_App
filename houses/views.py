# # from math import ceil
# # from django.core.paginator import Paginator
# # from django.shortcuts import render
# from django.shortcuts import render, redirect
# from django.core.paginator import Paginator, EmptyPage
# from . import models
# import houses


# def all_houses(request):
#     # page = request.GET.get("page", 1)
#     # page = int(page or 1)
#     # page_size = 10
#     # limit = page_size * page
#     # offset = limit - page_size
#     # all_houses = models.House.objects.all()[offset:limit]
#     # page_count = ceil(models.House.objects.count() / page_size)
#     # return render(
#     #     request,
#     #     "home.html",
#     #     context={
#     #         "houses": all_houses,
#     #         "page": page,
#     #         "page_count": page_count,
#     #         "page_range": range(1, page_count),
#     #     },
#     # )
#     # page = request.GET.get("page")
#     page = request.GET.get("page", 1)
#     house_list = models.House.objects.all()
#     # paginator = Paginator(house_list, 10)
#     # houses = paginator.get_page(page)
#     # return render(request, "home.html", {"houses": houses})
#     paginator = Paginator(house_list, 10, orphans=5)
#     # houses = paginator.page(int(page))
#     # return render(request, "home.html", {"page": houses})
#     try:
#         houses = paginator.page(int(page))
#         return render(request, "home.html", {"page": houses})
#     except EmptyPage:
#         return redirect("/")

from django.utils import timezone

# from django.views.generic import ListView
# from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django_countries import countries
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.House
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "houses"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


# def house_detail(request, pk):
#     try:
#         house = models.House.objects.get(pk=pk)
#         return render(request, "houses/detail.html", {"house": house})
#     except models.House.DoesNotExist:
#         raise Http404()


class HouseDetail(DetailView):

    """HouseDetail Definition"""

    model = models.House


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    house_types = models.HouseType.objects.all()
    return render(
        request,
        "houses/search.html",
        {"city": city, "countries": countries, "house_types": house_types},
    )
