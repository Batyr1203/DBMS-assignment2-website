from django.urls import path

from .views import HomePageView, DiseaseTypeListView


urlpatterns = [
    path('disease_types/', DiseaseTypeListView.as_view(), name='disease_type_list'),
    path('', HomePageView.as_view(), name='home'),
]
