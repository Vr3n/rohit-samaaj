from django.urls import path
from . import views

urlpatterns = [
    path('', views.SurveyTermsPage.as_view(), name='survey-home'),
]