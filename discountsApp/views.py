
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from . import views
import datetime
from django.utils import timezone
from .models import Product
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# from .forms import signUpForm
# from .models import User

# Create your views here.


def main_page(request):
    return render(request, 'discountsApp/mainPage.html')


def index(request):
    latest_item_list = Product.objects.order_by('PubTime')
    endding_item_list = Product.objects.order_by('EndTime')
    TodaySpecial =[]
    lastChance =[]
    luxury =[]
    electronic_product=[]
    clothing=[]
    now =timezone.now()
    for i in range(len(latest_item_list)):
        if len(TodaySpecial)==4  and len(luxury)==4 and len(electronic_product) ==4 and len(clothing) ==4:
            break
        else:
            if latest_item_list[i].Tag == 'Luxury' and len(luxury)<4:
                luxury.append(latest_item_list[i])
            if latest_item_list[i].Tag == 'electronic product' and len(electronic_product)<4:
                electronic_product.append(latest_item_list[i])
            if latest_item_list[i].Tag == 'Clothing' and len(clothing)<4:
                clothing.append(latest_item_list[i])
            if now - latest_item_list[i].PubTime < datetime.timedelta(days=1) and len(TodaySpecial)<4:
                TodaySpecial.append(latest_item_list[i])
    for j in range(len(endding_item_list)):
        if endding_item_list[j].EndTime - datetime.timedelta(days=2)< now and len(lastChance)<4:
                lastChance.append(endding_item_list[j])

    context ={
        'latest_item_list':latest_item_list,
        'lastChance':lastChance,
        'TodaySpecial':TodaySpecial,
        'luxury':luxury,
        'electronic_product':electronic_product,
        'clothing':clothing,

    }
    return render(request,'discountsApp/index.html',context)


def allPorduct(request):
    item_list = Product.objects.order_by('PubTime')

    
    # paginator = Paginator(item_list,2)


    # page = request.GET.get('page') 
    # try:
    #     item_list = paginator.page(page)  
    # except PageNotAnInteger:  
    #     item_list = paginator.page(1) 
    # except EmptyPage:  
    #     item_list = paginator.page(paginator.num_pages)  

    context={
        'item_list':item_list,
    }  
    return render(request,'discountsApp/all.html',context)

def luxury(request):
    item_list = Product.objects.all()
    luxury =[]

    for item in item_list:
        if item.Tag == 'Luxury':
            luxury.append(item)
    
    paginator = Paginator(luxury,2)
    #luxury_item_list = paginator.page(1)

    page = request.GET.get('page') 
    try:
        luxury = paginator.page(page)  
    except PageNotAnInteger:  
        luxury = paginator.page(1) 
    except EmptyPage:  
        luxury = paginator.page(paginator.num_pages)  

    context={
        'luxury':luxury,
    }  
    return render(request,'discountsApp/luxury.html',context)


def electronic (request):
    item_list = Product.objects.all()
    electronic  =[]

    for item in item_list:
        if item.Tag == 'electronic product':
            electronic.append(item)
    
    paginator = Paginator(electronic,2)
    #luxury_item_list = paginator.page(1)

    page = request.GET.get('page') 
    try:
        electronic = paginator.page(page)  
    except PageNotAnInteger:  
        electronic = paginator.page(1) 
    except EmptyPage:  
        electronic = paginator.page(paginator.num_pages)  

    context={
        'electronic':electronic,
    }  
    return render(request,'discountsApp/electronic.html',context)

def clothing (request):
    item_list = Product.objects.all()
    clothing  =[]

    for item in item_list:
        if item.Tag == 'Clothing':
            clothing.append(item)
    
    paginator = Paginator(clothing,2)
    #luxury_item_list = paginator.page(1)

    page = request.GET.get('page') 
    try:
        clothing = paginator.page(page)  
    except PageNotAnInteger:  
        clothing = paginator.page(1) 
    except EmptyPage:  
        clothing = paginator.page(paginator.num_pages)  

    context={
        'clothing':clothing,
    }  
    return render(request,'discountsApp/clothing.html',context)


def lastChancePage(request):
    endding_item_list = Product.objects.order_by('EndTime')
    lastchance  =[]
    now =timezone.now()
    for item in endding_item_list:
        if item.EndTime - datetime.timedelta(days=2)< now:
                lastchance.append(item)
    # paginator = Paginator(clothing,2)
    # #luxury_item_list = paginator.page(1)

    # page = request.GET.get('page') 
    # try:
    #     lastchance = paginator.page(page)  
    # except PageNotAnInteger:  
    #     lastchance = paginator.page(1) 
    # except EmptyPage:  
    #     lastchance = paginator.page(paginator.num_pages)  

    context={
        'lastchance':lastchance,
    }  
    return render(request,'discountsApp/lastChance.html',context)


def login(request):
    return render(request, 'discountsApp/login.html')


def signup(request):
 
    return render(request, 'discountsApp/signUp.html')


def forgotPassword(request):
    return render(request, 'discountsApp/forgotPassword.html')


def product(request):
    return render(request,'discountsApp/product.html')
