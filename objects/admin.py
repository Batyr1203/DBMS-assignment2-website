from django.contrib import admin

from .models import DiseaseType, Disease


admin.site.register(DiseaseType)
admin.site.register(Disease)
