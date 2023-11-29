from django.urls import path
from . import views
from django.urls import include

urlpatterns = [
    path('',views.index,name='index'),
    path(r'^vaccine_status/$',views.vaccine_status,name='vaccine_status'),
    path(r'^beds_status/$',views.bed_status,name='beds_status'),
    path(r'^oxygen_status/$',views.oxygen_status,name='oxygen_status'),
    path(r'^hospital_status/$',views.hospital_status,name='hospital_status'),
    path('signup',views.signup, name='signup'),
]
