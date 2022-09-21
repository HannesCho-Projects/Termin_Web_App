from django.urls import path
from . import views

app_name = "houses"

# urlpatterns = [path("<int:pk>", views.house_detail, name="detail")]
urlpatterns = [
    path("<int:pk>", views.HouseDetail.as_view(), name="detail"),
    path("search/", views.SearchView.as_view(), name="search"),
]
