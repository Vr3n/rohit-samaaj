from django.views.generic import TemplateView
from formtools.wizard.views import SessionWizardView
from django.shortcuts import render
from .models import SamaajMember
from .forms import (
    SamaajMemberForm,
)

# Create your views here.


class SurveyTermsPage(TemplateView):
    template_name = "survey/index.html"
