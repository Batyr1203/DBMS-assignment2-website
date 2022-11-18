from django.urls import path

from .views import (
    HomePageView,
    DiseaseTypeListView, DiseaseTypeUpdateView, DiseaseTypeDeleteView, DiseaseTypeCreateView, list_diseases_by_type,
    DiseaseListView, DiseaseDetailView, DiseaseUpdateView, DiseaseDeleteView, DiseaseCreateView,
    CountryListView, CountryDetailView, CountryUpdateView, CountryDeleteView, CountryCreateView,
)


urlpatterns = [
    path('countries/new', CountryCreateView.as_view(), name='country_new'),
    path('countries/<str:pk>/edit', CountryUpdateView.as_view(), name='country_edit'),
    path('countries/<str:pk>/delete', CountryDeleteView.as_view(), name='country_delete'),
    path('countries/<str:pk>/', CountryDetailView.as_view(), name='country_detail'),
    path('countries/', CountryListView.as_view(), name='country_list'),

    path('diseases/new/', DiseaseCreateView.as_view(), name='disease_new'),
    path('diseases/<str:pk>/edit/', DiseaseUpdateView.as_view(), name='disease_edit'),
    path('diseases/<str:pk>/delete/', DiseaseDeleteView.as_view(), name='disease_delete'),
    path('diseases/<str:pk>/', DiseaseDetailView.as_view(), name='disease_detail'),
    path('diseases/', DiseaseListView.as_view(), name='disease_list'),

    path('disease_types/<int:pk>/diseases/', list_diseases_by_type, name='disease_type_diseases'),
    path('disease_types/<int:pk>/edit/', DiseaseTypeUpdateView.as_view(), name='disease_type_edit'), 
    path('disease_types/<int:pk>/delete/', DiseaseTypeDeleteView.as_view(), name='disease_type_delete'),
    path('disease_types/new/', DiseaseTypeCreateView.as_view(), name='disease_type_new'),
    path('disease_types/', DiseaseTypeListView.as_view(), name='disease_type_list'),
    
    path('', HomePageView.as_view(), name='home'),
]
