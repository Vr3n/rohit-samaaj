from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


def home(request):
    return redirect(reverse('survey-home'))


def hello_htmx(request):
    return render(request, "partials/htmx_test.html")
