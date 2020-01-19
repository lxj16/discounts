
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from . import views
# from .forms import signUpForm
# from .models import User

# Create your views here.


def main_page(request):
    return render(request, 'discountsApp/mainPage.html')


def index(request):
    return render(request, 'discountsApp/index.html')


def login(request):
    return render(request, 'discountsApp/login.html')


def signup(request):
    # form = signUpForm(request.POST or None)

    # if request.method == 'POST' and form.is_valid():
    #     new_user = form.save()
    #     return HttpResponseRedirect('/')
    # form = forms.signUpForm()
    # if request == 'POST':
    #     form = forms.signUpForm(request.POST)
    #     if form.is_valid():

    #         user_name = form.cleaned_data.get('user_name')
    #         email = form.cleaned_data.get('email')
    #         password = form.cleaned_data.get('password')
    #         new_user = User(name=user_name, password=password, email=email)
    #         new_user.save()

    #     else:
    #         form = forms.signUpForm()
    # return render(request, 'discountsApp/signUp.html', {'form': form})
    return render(request, 'discountsApp/signUp.html')


def forgotPassword(request):
    return render(request, 'discountsApp/forgotPassword.html')
