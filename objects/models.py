from django.db import models
from django.urls import reverse


class DiseaseType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse('disease_type_detail', kwargs={'pk': self.pk})


class Disease(models.Model):
    disease_code = models.CharField(max_length=50, primary_key=True)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.disease_code

