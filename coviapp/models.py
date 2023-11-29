from django.db import models
from django.urls import reverse
# Create your models here.

class Hospital(models.Model):
    name=models.CharField(max_length=200,help_text='hospital name')
    Address=models.CharField(max_length=200,help_text='hospital city')
    pincode=models.CharField(max_length=10,help_text='6-digits pincode of city')
    hospital_id=models.IntegerField(primary_key=True)
    class Meta:
        ordering=['name']

    def get_absolute_url(self):
        return reverse('Hospital-details', args=[str(self.hospital_id)])

    def __str__(self):
        return self.name

class Vaccine(models.Model):
    hospital=models.ForeignKey('Hospital',on_delete=models.SET_NULL,null=True, unique=True)
    vaccine_name=models.CharField(null=True,max_length=30,help_text='name of vaccine')
    amount_dose_1=models.IntegerField(null=True,help_text='available amount of Dose 1')
    amount_dose_2=models.IntegerField(null=True,help_text='available amount of Dose 2')
    cost_dose_1=models.IntegerField(null=True,help_text='cost of dose 1 per dose')
    cost_dose_2 = models.IntegerField(null=True,help_text='cost of dose 2 per dose')

class Oxygen(models.Model):
    hospital=models.ForeignKey('Hospital',on_delete=models.SET_NULL, null=True, unique=True)
    amount=models.IntegerField(help_text='available amount')
    cost=models.IntegerField(help_text='cost per cylinder')

class Bed(models.Model):
    hospital_id=models.ForeignKey('Hospital',on_delete=models.SET_NULL, null=True,unique=True)
    amount=models.IntegerField(help_text='no of available beds')
    cost=models.IntegerField(help_text='cost per bed')

class Patient(models.Model):
    first_name=models.CharField(max_length=20,help_text='first name of patient')
    last_name=models.CharField(max_length=20,help_text='last name of patient')
    city=models.CharField(max_length=100,help_text='patient city')
    pincode=models.CharField(max_length=10,help_text='pincode of patient city')
    patient_id=models.IntegerField(primary_key=True,help_text='unique id of patient')

    class Meta:
        ordering=['first_name','last_name']

    def get_absolute_url(self):
        return reverse('Patient-details', args=[str(self.patient_id)])

    def __str__(self):
        return self.first_name