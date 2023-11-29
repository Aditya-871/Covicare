from django.shortcuts import render
from .models import Vaccine,Bed,Oxygen,Hospital
from .filter import vaccineFilter,bedsFilter,oxygenFilter,hospitalFilter
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm

# Create your views here.
def index(request):
    return render(request,'coviapp/index.html')

def vaccine_status(request):
    vaccine_list = Vaccine.objects.all()
    user_filter = vaccineFilter(request.GET, queryset=vaccine_list)
    return render(request, 'coviapp/vaccine_page.html', {'filter': user_filter})


def bed_status(request):
    bed_list = Bed.objects.all()
    bed_filter = bedsFilter(request.GET, queryset=bed_list)
    return render(request,'coviapp/beds_page.html',{'filter': bed_filter})

def oxygen_status(request):
    oxygen_list = Oxygen.objects.all()
    oxygen_filter = oxygenFilter(request.GET, queryset = oxygen_list)
    return render(request,'coviapp/oxygen_page.html',{'filter' : oxygen_filter})

def hospital_status(request):
    hospital_list = Hospital.objects.all()
    hospital_filter = hospitalFilter(request.GET, queryset = hospital_list)
    return render(request, 'coviapp/hospital_page.html',{'filter' : hospital_filter})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'coviapp/sign_up.html', {'form': form})