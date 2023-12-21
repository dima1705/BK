from django.shortcuts import render, get_object_or_404
from .models import Burger
from cart.forms import CartAddProductForm
# Create your views here.


def burgers(request):

    cart_product_form = CartAddProductForm()

    context = {
        'burgers': Burger.objects.all(),
        'cart_product_form': cart_product_form
    }

    return render(
        request,
        'products/burgers.html',
        context
    )


def burger_card(request, burger_id):
    burger = get_object_or_404(
        Burger,
        pk=burger_id,
    )

    cart_product_form = CartAddProductForm()
    context = {
        'burger': burger,
        'cart_product_form': cart_product_form
    }
    return render(
        request,
        'products/burger_card.html',
        context
    )