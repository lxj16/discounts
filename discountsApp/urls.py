from django.urls import path
from . import views

app_name = 'discountsApp'
urlpatterns = [
    path('', views.index, name='discounts-main'),
    # path('login/', views.login),
    # path('signup/', views.signup),
    # path('forgotpassword/', views.forgotPassword),
    #path('product/',views.product),
    path('all/',views.allPorduct),
    path('luxury/',views.luxury),
    path('electronic/',views.electronic),
    path('clothing/',views.clothing),
    path('lastChance/',views.lastChancePage),
]
