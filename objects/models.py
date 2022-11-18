from django.db import models
from django.urls import reverse


class DiseaseType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=140)

    def __str__(self):
        return str(self.id)

    # def get_absolute_url(self):
    #     return reverse('disease_type_detail', kwargs={'pk': self.pk})


class Country(models.Model):
    class Meta:
        verbose_name_plural = "Countries"

    cname = models.CharField(max_length=50, primary_key=True)
    population = models.PositiveBigIntegerField()

    def __str__(self):
        return self.cname

    def get_absolute_url(self):
        return reverse('country_detail', kwargs={'pk': self.pk})



class Disease(models.Model):
    disease_code = models.CharField(max_length=50, primary_key=True)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)

    def __str__(self):
        return self.disease_code

    def get_absolute_url(self):
        return reverse('disease_detail', kwargs={'pk': self.pk})


class Discover(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    disease_code = models.ForeignKey(Disease, on_delete=models.CASCADE)
    first_enc = models.DateField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['cname', 'disease_code'], name='unique_cname_disease_code_combination'
            )
        ]

    def __str__(self):
        return str(self.cname) + '-' + str(self.disease_code)


class User(models.Model):
    email = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.PositiveIntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'pk': self.pk})




