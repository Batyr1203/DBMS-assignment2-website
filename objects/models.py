from django.db import models
from django.urls import reverse


class DiseaseType(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('disease_type_detail', kwargs={'pk': self.pk})
