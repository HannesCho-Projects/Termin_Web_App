from django.urls import path
from houses import views as house_views

app_name = "core"

# urlpatterns = [path("", house_views.all_houses, name="home")]
urlpatterns = [path("", house_views.HomeView.as_view(), name="home")]
