from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def hello_htmx(request):
    return render(request, "partials/htmx_test.html")
