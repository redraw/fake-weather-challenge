from django.urls import path
from api import views


urlpatterns = [path("temp/", views.TemperatureView.as_view())]
