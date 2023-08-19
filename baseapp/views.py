from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime


# Create your views here.

def homePage(request):
    return render(request, 'baseapp/homePage.html')


def basePage(request):
    return render(request, 'baseapp/basePage.html')


def errorPage(request):
    return render(request, 'baseapp/page_404.html')


def showallFlightData(request):

    if request.method == 'POST':
        params = {
        'access_key': '3d85882033e37eea9aa6b573fb216635'
        }
        # the url for current weather, takes city_name and API_KEY   
        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
        # converting the request response to json   
        response = api_result.json()
        my_res = response['data']
        # bundling the weather information in one dictionary
        flight_update = {
            'datas': my_res
        }
        return render(request, 'baseapp/show.html', flight_update)
    # if the request method is GET empty the dictionary
    else:
        flight_update = {}
    context = {'flight_update': flight_update}
    return render(request, 'baseapp/show.html', context)

def showAirlines(request):

    if request.method == 'POST':
        # getting the city name from the form input   
        airline = request.POST.get('airline')
        params = {
        'access_key': '3d85882033e37eea9aa6b573fb216635'
        }

        # the url for current weather, takes city_name and API_KEY   
        api_result = requests.get('http://api.aviationstack.com/v1/airlines', params)
        # converting the request response to json   
        response = api_result.json()
        my_res = response['data']
        # bundling the weather information in one dictionary
        airlines = {
            'datas': my_res
        }
        return render(request, 'baseapp/airlineData.html', airlines)
    # if the request method is GET empty the dictionary
    else:
        airlines = {}
    context = {'airlines': airlines}
    return render(request, 'baseapp/airlineData.html', context)




def showCountries(request):

    if request.method == 'POST':
        # getting the city name from the form input   
        airline = request.POST.get('airline')
        params = {
        'access_key': '3d85882033e37eea9aa6b573fb216635'
        }

        # the url for current weather, takes city_name and API_KEY   
        api_result = requests.get('http://api.aviationstack.com/v1/countries', params)
        # converting the request response to json   
        response = api_result.json()
        my_res = response['data']
        # bundling the weather information in one dictionary
        countries = {
            'datas': my_res
        }
        return render(request, 'baseapp/countriesData.html', countries)
    # if the request method is GET empty the dictionary
    else:
        countries = {}
    context = {'countries': countries}
    return render(request, 'baseapp/countriesData.html', context)




def showCities(request):

    if request.method == 'POST':
        # getting the city name from the form input   
        airline = request.POST.get('airline')
        params = {
        'access_key': '3d85882033e37eea9aa6b573fb216635'
        }

        # the url for current weather, takes city_name and API_KEY   
        api_result = requests.get('http://api.aviationstack.com/v1/cities', params)
        # converting the request response to json   
        response = api_result.json()
        my_res = response['data']
        # bundling the weather information in one dictionary
        cities = {
            'datas': my_res
        }
        return render(request, 'baseapp/citiesData.html', cities)
    # if the request method is GET empty the dictionary
    else:
        cities = {}
    context = {'cities': cities}
    return render(request, 'baseapp/citiesData.html', context)





def showAirplanes(request):

    if request.method == 'POST':
        # getting the city name from the form input   
        airline = request.POST.get('airline')
        params = {
        'access_key': '3d85882033e37eea9aa6b573fb216635'
        }

        # the url for current weather, takes city_name and API_KEY   
        api_result = requests.get('http://api.aviationstack.com/v1/airplanes', params)
        # converting the request response to json   
        response = api_result.json()
        my_res = response['data']
        # bundling the weather information in one dictionary
        airplane = {
            'datas': my_res
        }
        return render(request, 'baseapp/airplaneData.html', airplane)
    # if the request method is GET empty the dictionary
    else:
        cities = {}
    context = {'cities': cities}
    return render(request, 'baseapp/airplaneData.html', context)




def showAirports(request):

    if request.method == 'POST':
        # getting the city name from the form input   
        airline = request.POST.get('airline')
        params = {
        'access_key': '3d85882033e37eea9aa6b573fb216635'
        }

        # the url for current weather, takes city_name and API_KEY   
        api_result = requests.get('http://api.aviationstack.com/v1/airports', params)
        # converting the request response to json   
        response = api_result.json()
        my_res = response['data']
        # bundling the weather information in one dictionary
        airports = {
            'datas': my_res
        }
        return render(request, 'baseapp/airportsData.html', airports)
    # if the request method is GET empty the dictionary
    else:
        airports = {}
    context = {'airports': airports}
    return render(request, 'baseapp/airportsData.html', context)








