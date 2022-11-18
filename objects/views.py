from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import DiseaseType, Disease, Country, Discover, User


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


# class DiseaseTypeDiseasesListView(ListView):
#     model = Disease
#     template_name = 'disease_type/disease_type_diseases.html'

def list_diseases_by_type(request, pk):
    diseases = Disease.objects.filter(id=pk)
    template = loader.get_template('disease_type/disease_type_diseases.html')
    context = {
        'disease_type_id': pk,
        'disease_type': DiseaseType.objects.get(id=pk).description,
        'diseases': diseases,
    }    
    return HttpResponse(template.render(context, request))



#################################### COUNTRY ###############################################

class CountryListView(ListView):
    model = Country
    template_name = 'country/country_list.html'


class CountryDetailView(DetailView):
    model = Country
    template_name = 'country/country_detail.html'


class CountryUpdateView(UpdateView):
    model = Country
    fields = ('cname', 'population')
    template_name = 'country/country_edit.html'


class CountryDeleteView(DeleteView):
    model = Country
    template_name = 'country/country_delete.html'
    success_url = reverse_lazy('country_list')


class CountryCreateView(CreateView):
    model = Country
    template_name = 'country/country_new.html'
    fields = ('cname', 'population')


#################################### DISEASE ###############################################

class DiseaseListView(ListView):
    model = Disease
    template_name = 'disease/disease_list.html'


class DiseaseDetailView(DetailView):
    model = Disease
    template_name = 'disease/disease_detail.html'


class DiseaseUpdateView(UpdateView):
    model = Disease
    fields = ('disease_code', 'pathogen', 'description', 'id',)
    template_name = 'disease/disease_edit.html'
    success_url = reverse_lazy('disease_list')


class DiseaseDeleteView(DeleteView):
    model = Disease
    template_name = 'disease/disease_delete.html'
    success_url = reverse_lazy('disease_list')


class DiseaseCreateView(CreateView):
    model = Disease
    template_name = 'disease/disease_new.html'
    fields = ('disease_code', 'pathogen', 'description', 'id',)
#    success_url = reverse_lazy('disease_list')


#################################### DISEASE ###############################################

class DiscoverListView(ListView):
    model = Discover
    template_name = 'discover/discover_list.html'


class DiscoverUpdateView(UpdateView):
    model = Discover
    template_name = 'discover/discover_edit.html'
    fields = ('cname', 'disease_code', 'first_enc',)
    success_url = reverse_lazy('discover_list')


class DiscoverDeleteView(DeleteView):
    model = Discover
    template_name = 'discover/discover_delete.html'
    success_url = reverse_lazy('discover_list')


class DiscoverCreateView(CreateView):
    model = Discover
    template_name = 'discover/discover_new.html'
    fields = ('cname', 'disease_code', 'first_enc',)
    success_url = reverse_lazy('discover_list')


#################################### DISEASE ###############################################

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'


class UserDetailView(DetailView):
    model = User
    template_name = 'user/user_detail.html'


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user/user_edit.html'
    fields = ('email', 'name', 'surname', 'salary', 'phone', 'cname')
 

class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/user_delete.html'
    success_url = reverse_lazy('user_list')


class UserCreateView(CreateView):
    model = User 
    template_name = 'user/user_new.html'
    fields = ('email', 'name', 'surname', 'salary', 'phone', 'cname')
