from django.views.generic import TemplateView, ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import DiseaseType, Disease



class HomePageView(TemplateView):
    template_name = 'home.html'

#################################### DISEASE_TYPE ###############################################

class DiseaseTypeListView(ListView):
    model = DiseaseType
    template_name = 'disease_type/disease_type_list.html'


class DiseaseTypeUpdateView(UpdateView):
    model = DiseaseType
    fields = ('description',)
    template_name = 'disease_type/disease_type_edit.html'
    success_url = reverse_lazy('disease_type_list')


class DiseaseTypeDeleteView(DeleteView):
    model = DiseaseType
    template_name = 'disease_type/disease_type_delete.html'
    success_url = reverse_lazy('disease_type_list')


class DiseaseTypeCreateView(CreateView):
    model = DiseaseType
    template_name = 'disease_type/disease_type_new.html'
    fields = ('description',)
    success_url = reverse_lazy('disease_type_list')



#################################### DISEASE ###############################################

class DiseaseListView(ListView):
    model = Disease
    template_name = 'disease/disease_list.html'
