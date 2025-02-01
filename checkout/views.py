from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('art'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QnTQ5LDUEz8eXIQZKuBkJmEU35DeUan4md0Ltt9sC1RcPDjjHXSjFOx1Qzh01ckAUQ03vdvLt4rKJSeJBdm1bBS00AevoNSXI',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
