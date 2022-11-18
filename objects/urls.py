from django.urls import path

from .views import (
    HomePageView,
    DiseaseTypeListView, DiseaseTypeUpdateView, DiseaseTypeDeleteView, DiseaseTypeCreateView,
    DiseaseListView,
)


urlpatterns = [
    path('diseases/', DiseaseListView.as_view(), name='disease_list'),

    path('disease_types/<int:pk>/edit/', DiseaseTypeUpdateView.as_view(), name='disease_type_edit'), 
    path('disease_types/<int:pk>/delete/', DiseaseTypeDeleteView.as_view(), name='disease_type_delete'),
    path('disease_types/new/', DiseaseTypeCreateView.as_view(), name='disease_type_new'),
    path('disease_types/', DiseaseTypeListView.as_view(), name='disease_type_list'),
    
    path('', HomePageView.as_view(), name='home'),
]
