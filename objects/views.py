from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import DiseaseType, Disease, Country, Discover, User, PublicServant, Doctor, Specialize, Record


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


#################################### USER ###############################################

class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'


def list_users(request):
    users = User.objects.all()
    ps_emails = [ps.email.email for ps in PublicServant.objects.all()]
    ds_emails = [ds.email.email for ds in Doctor.objects.all()]
    template = loader.get_template('user/user_list.html')
    context = {
        'user_list': users,
        'ps_emails': ps_emails,
        'ds_emails': ds_emails,
    }
    return HttpResponse(template.render(context, request))


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


#################################### PUBLIC SERVANT and DOCTOR ##############################################

class PublicServantUpdateView(UpdateView):
    model = PublicServant
    template_name = 'user/ps_edit.html'
    fields = ('department',)
    success_url = reverse_lazy('user_list')


class PublicServantDeleteView(DeleteView):
    model = PublicServant
    template_name = 'user/ps_delete.html'
    success_url = reverse_lazy('user_list')


class PublicServantCreateView(CreateView):
    model = PublicServant
    template_name = 'user/ps_new.html'
    fields = ('email', 'department',)



##############################################################################################################

class DoctorUpdateView(UpdateView):
    model = Doctor
    template_name = 'user/d_edit.html'
    fields = ('degree',)
    success_url = reverse_lazy('user_list')


class DoctorDeleteView(DeleteView):
    model = Doctor
    template_name = 'user/d_delete.html'
    success_url = reverse_lazy('user_list')


class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'user/d_new.html'
    fields = ('email', 'degree',)


#################################### SPECIALIZE ###############################################

class SpecializeListView(ListView):
    model = Specialize
    template_name = 'specialize/specialize_list.html'


class SpecializeUpdateView(UpdateView):
    model = Specialize
    template_name = 'specialize/specialize_edit.html'
    fields = ('disease_type_id', 'email')
    success_url = reverse_lazy('specialize_list')


class SpecializeDeleteView(DeleteView):
    model = Specialize
    template_name = 'specialize/specialize_delete.html'
    success_url = reverse_lazy('specialize_list')


class SpecializeCreateView(CreateView):
    model = Specialize
    template_name = 'specialize/specialize_new.html'
    fields = ('disease_type_id', 'email')
    success_url = reverse_lazy('specialize_list')


#################################### RECORD ###############################################

class RecordListView(ListView):
    model = Record
    template_name = 'record/record_list.html'


class RecordDetailView(DetailView):
    model = Record
    template_name = 'record/record_detail.html'


class RecordUpdateView(UpdateView):
    model = Record
    template_name = 'record/record_edit.html'
    fields = ('email', 'cname', 'disease_code', 'total_deaths', 'total_patients')


class RecordDeleteView(DeleteView):
    model = Record
    template_name = 'record/record_delete.html'
    success_url = reverse_lazy('record_list')


class RecordCreateView(CreateView):
    model = Record
    template_name = 'record/record_new.html'
    fields = ('email', 'cname', 'disease_code', 'total_deaths', 'total_patients')
