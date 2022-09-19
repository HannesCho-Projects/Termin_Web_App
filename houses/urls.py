from django.urls import path
from . import views

app_name = "houses"

urlpatterns = [path("<int:pk>", views.house_detail, name="detail")]
