from django.views.generic import TemplateView, ListView

from .models import DiseaseType


class HomePageView(TemplateView):
    template_name = 'home.html'


class DiseaseTypeListView(ListView):
    model = DiseaseType
    template_name = 'disease_type/disease_type_list.html'

