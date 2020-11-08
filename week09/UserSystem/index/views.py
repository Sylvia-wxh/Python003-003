from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.http import HttpResponseNotFound

from django.http import HttpResponse
from .models import PersonList
from .form import LoginForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# Create your views here.

def login1(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user:
                login(request, user)
                # return HttpResponse('login success')
                return redirect('/home')
            else:
                return HttpResponse('login fail')
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'form1.html', {'form': login_form})

def home(request):
    return HttpResponse('Welcome Home!')


# @csrf_exempt
# def result(request):
#     return render(request, 'result.html')