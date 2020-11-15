from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from .models import shampoo_senti
from .home_form import HomeForm
from requests import post

# Create your views here.

def home(request):
    search = request.POST.get('search', '')
    return render(request, 'home.html', {'form': HomeForm} )