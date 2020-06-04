from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        message.error(request, "There is nothing in your bag right now")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51GqJ5EHKfLOwRnJ3XFXbQ8xlzVlnViREL22CaqdLVUKpK4noXLjrl6HawbOUuIXQUZw3gg1Ib8pPuvIqQk4Pag1D00mheCMCdh',
        'client_secret': 'test_user',
    }

    return render(request, template, context)