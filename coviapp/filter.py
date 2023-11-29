from django.contrib.auth.models import User
import django_filters
from .models import Vaccine,Bed,Oxygen,Hospital

class vaccineFilter(django_filters.FilterSet):
    class Meta:
        model = Vaccine
        fields = {
            'vaccine_name': ['iexact', ],
            'hospital__pincode': ['iexact', ],
        }


class bedsFilter(django_filters.FilterSet):
    class Meta:
        model= Bed
        fields = {
            'amount': ['gte', ],
            'hospital_id__pincode': ['iexact', ],
        }


class oxygenFilter(django_filters.FilterSet):
    class Meta:
        model= Oxygen
        fields = {
            'amount': ['gte', ],
            'hospital_id__pincode': ['iexact', ],
        }

class hospitalFilter(django_filters.FilterSet):
    class Meta:
        model= Hospital
        fields = {
           'name': ['iexact', ],
           'pincode': ['iexact', ],
        }