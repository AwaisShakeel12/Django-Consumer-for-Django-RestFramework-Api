from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.http import HttpResponse


# Create your views here.

def home(request):

    api_url = 'http://127.0.0.1:8000/'

    response = requests.get(api_url)

    data = response.json()

    return JsonResponse(data, safe=False)


def cars(request):
    api_url = 'http://127.0.0.1:8000/'

    response = requests.get(api_url)

    data = response.json()

    cars = data['vehicles']

    context = {'cars':cars}


    return render(request, 'home.html', context)
