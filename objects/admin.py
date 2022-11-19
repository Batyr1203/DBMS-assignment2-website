from django.contrib import admin

from .models import DiseaseType, Disease, Country, Discover, User, PublicServant, Doctor


admin.site.register(DiseaseType)
admin.site.register(Disease)
admin.site.register(Country)
admin.site.register(Discover)
admin.site.register(User)
admin.site.register(PublicServant)
admin.site.register(Doctor)
