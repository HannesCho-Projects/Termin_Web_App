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
from django.views.generic import ListView, DetailView, View
from django_countries import countries
from . import models, forms


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


class SearchView(View):

    """SearchView Definition"""

    def get(self, request):

        country = request.GET.get("country")

        if country:

            form = forms.SearchForm(request.GET)

            if form.is_valid():

                city = form.cleaned_data.get("city")
                country = form.cleaned_data.get("country")
                house_type = form.cleaned_data.get("house_type")
                price = form.cleaned_data.get("price")
                guests = form.cleaned_data.get("guests")
                bedrooms = form.cleaned_data.get("bedrooms")
                beds = form.cleaned_data.get("beds")
                baths = form.cleaned_data.get("baths")
                instant_book = form.cleaned_data.get("instant_book")
                superhost = form.cleaned_data.get("superhost")
                amenities = form.cleaned_data.get("amenities")
                facilities = form.cleaned_data.get("facilities")

                filter_args = {}

                if city != "Anywhere":
                    filter_args["city__startswith"] = city

                filter_args["country"] = country

                if house_type is not None:
                    filter_args["house_type"] = house_type

                if price is not None:
                    filter_args["price__lte"] = price

                if guests is not None:
                    filter_args["guests__gte"] = guests

                if bedrooms is not None:
                    filter_args["bedrooms__gte"] = bedrooms

                if beds is not None:
                    filter_args["beds__gte"] = beds

                if baths is not None:
                    filter_args["baths__gte"] = baths

                if instant_book is True:
                    filter_args["instant_book"] = True

                if superhost is True:
                    filter_args["host__superhost"] = True

                for amenity in amenities:
                    filter_args["amenities"] = amenity

                for facility in facilities:
                    filter_args["facilities"] = facility

                houses = models.House.objects.filter(**filter_args)

                return render(
                    request, "houses/search.html", {"form": form, "houses": houses}
                )

        else:

            form = forms.SearchForm()
            houses = models.House.objects.filter()

            return render(
                request, "houses/search.html", {"form": form, "houses": houses}
            )


# Function base view below:

# def search(request):

#     form = forms.SearchForm()
#     return render(request, "houses/search.html", {"form": form})

# city = request.GET.get("city", "Anywhere")
# city = str.capitalize(city)
# country = request.GET.get("country", "DE")
# house_type = int(request.GET.get("house_type", 0))
# price = int(request.GET.get("price", 0))
# guests = int(request.GET.get("guests", 0))
# bedrooms = int(request.GET.get("bedrooms", 0))
# beds = int(request.GET.get("beds", 0))
# baths = int(request.GET.get("baths", 0))
# s_amenities = request.GET.getlist("amenities")
# s_facilities = request.GET.getlist("facilities")
# instant = bool(request.GET.get("instant", False))
# superhost = bool(request.GET.get("superhost", False))

# form = {
#     "city": city,
#     "s_house_type": house_type,
#     "s_country": country,
#     "price": price,
#     "guests": guests,
#     "bedrooms": bedrooms,
#     "beds": beds,
#     "baths": baths,
#     "s_amenities": s_amenities,
#     "s_facilities": s_facilities,
#     "instant": instant,
#     "superhost": superhost,
# }

# house_types = models.HouseType.objects.all()
# amenities = models.Amenity.objects.all()
# facilities = models.Facility.objects.all()

# choices = {
#     "countries": countries,
#     "house_types": house_types,
#     "amenities": amenities,
#     "facilities": facilities,
# }

# filter_args = {}

# if city != "Anywhere":
#     filter_args["city__startswith"] = city

# filter_args["country"] = country

# if house_type != 0:
#     filter_args["room_type__pk"] = house_type

# if price != 0:
#     filter_args["price__lte"] = price

# if guests != 0:
#     filter_args["guests__gte"] = guests

# if bedrooms != 0:
#     filter_args["bedrooms__gte"] = bedrooms

# if beds != 0:
#     filter_args["beds__gte"] = beds

# if baths != 0:
#     filter_args["baths__gte"] = baths

# if instant is True:
#     filter_args["instant_book"] = True

# if superhost is True:
#     filter_args["host__superhost"] = True

# if len(s_amenities) > 0:
#     for s_amenity in s_amenities:
#         filter_args["amenities__pk"] = int(s_amenity)

# if len(s_facilities) > 0:
#     for s_facility in s_facilities:
#         filter_args["facilities__pk"] = int(s_facility)

# houses = models.House.objects.filter(**filter_args)

# return render(request, "houses/search.html", {**form, **choices, "houses": houses})
