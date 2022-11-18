from django.contrib import admin

from .models import DiseaseType, Disease, Country


admin.site.register(DiseaseType)
admin.site.register(Disease)
admin.site.register(Country)
