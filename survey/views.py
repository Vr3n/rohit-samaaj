from django.views.generic import TemplateView


# Create your views here.


class SurveyTermsPage(TemplateView):
    template_name = "survey/index.html"
