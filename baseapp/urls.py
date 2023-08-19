# here we are import path from in-built django-urls
from django.urls import path

# here we are importing all the Views from the views.py file
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('basePage', views.basePage, name='basePage'),
    path('errorPage', views.errorPage, name='errorPage'),
    path('/show-all', views.showallFlightData, name='show'),
    path('/show-airlines', views.showAirlines, name='airlines'),
    path('/show-airports', views.showAirports, name='airports'),
    path('/show-airplanes', views.showAirplanes, name='airplanes'),
    path('/show-countries', views.showCountries, name='countries'),
    path('/show-cities', views.showCities, name='cities'),
]
