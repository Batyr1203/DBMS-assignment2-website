from django.urls import path

from .views import (
    HomePageView,
    DiseaseTypeListView, DiseaseTypeUpdateView, DiseaseTypeDeleteView, DiseaseTypeCreateView, list_diseases_by_type,
    DiseaseListView, DiseaseDetailView, DiseaseUpdateView, DiseaseDeleteView, DiseaseCreateView,
    CountryListView, CountryDetailView, CountryUpdateView, CountryDeleteView, CountryCreateView,
    DiscoverListView, DiscoverUpdateView, DiscoverDeleteView, DiscoverCreateView,
    UserListView, UserDetailView, UserUpdateView, UserDeleteView, UserCreateView, list_users,
    PublicServantUpdateView, PublicServantDeleteView, PublicServantCreateView, 
    DoctorDeleteView, DoctorUpdateView, DoctorCreateView,
    SpecializeListView, SpecializeUpdateView, SpecializeDeleteView, SpecializeCreateView,
    RecordListView, RecordDetailView, RecordUpdateView, RecordDeleteView, RecordCreateView,
)


urlpatterns = [

    path('records/new/', RecordCreateView.as_view(), name='record_new'),
    path('records/<str:pk>/delete/', RecordDeleteView.as_view(), name='record_delete'),
    path('records/<str:pk>/edit/', RecordUpdateView.as_view(), name='record_edit'),
    path('records/<str:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('records/', RecordListView.as_view(), name='record_list'),

    path('specializes/<str:pk>/delete/', SpecializeDeleteView.as_view(), name='specialize_delete'),
    path('specializes/<str:pk>/edit/', SpecializeUpdateView.as_view(), name='specialize_edit'),
    path('specializes/new/', SpecializeCreateView.as_view(), name='specialize_new'),
    path('specializes/', SpecializeListView.as_view(), name='specialize_list'),

    path('public_servants/new', PublicServantCreateView.as_view(), name='public_servant_new'),
    path('doctors/new', DoctorCreateView.as_view(), name='doctor_new'),
    path('users/<str:pk>/doctor/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),
    path('users/<str:pk>/doctor/edit/', DoctorUpdateView.as_view(), name='doctor_edit'),
    path('users/<str:pk>/public_servant/delete/', PublicServantDeleteView.as_view(), name='public_servant_delete'),
    path('users/<str:pk>/public_servant/edit/', PublicServantUpdateView.as_view(), name='public_servant_edit'),
    
    path('users/<str:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
    path('users/<str:pk>/edit', UserUpdateView.as_view(), name='user_edit'),
    path('users/<str:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/new', UserCreateView.as_view(), name='user_new'),    
    # path('users/', UserListView.as_view(), name='user_list'),
    path('users/', list_users, name='user_list'),

    path('discoveries/new', DiscoverCreateView.as_view(), name='discover_new'),
    path('discoveries/<str:pk>/delete/', DiscoverDeleteView.as_view(), name='discover_delete'),
    path('discoveries/<str:pk>/edit/', DiscoverUpdateView.as_view(), name='discover_edit'),
    path('discoveries/', DiscoverListView.as_view(), name='discover_list'),

    path('countries/new', CountryCreateView.as_view(), name='country_new'),
    path('countries/<str:pk>/edit/', CountryUpdateView.as_view(), name='country_edit'),
    path('countries/<str:pk>/delete/', CountryDeleteView.as_view(), name='country_delete'),
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
