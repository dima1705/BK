from django.urls import path, include
from django.contrib import admin

from .views import burgers, burger_card

app_name = 'products'

urlpatterns = [
    path('', burgers, name='burgers'),
    path('burger/<int:burger_id>', burger_card, name='burger_card'),


    # path('baskets/add/<int:burger_id>/', basket_add, name='basket_add'),
    # path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]