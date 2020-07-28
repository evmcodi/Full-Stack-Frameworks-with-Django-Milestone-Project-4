from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.urls import reverse

from django.conf import settings


import stripe



@login_required
def view_payment(request):
    """ A view that renders the payment page template """

    user = request.user

    # Check if user has already paid and redirect them to definitions app.
    if user.has_perm('definitionssoftware.access_paid_definitions_app'):
        return redirect(reverse('view_definitionssoftware'))


    # Get stripe environment variables
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    # Create Stripe Payment Intent
    stripe_total = 2500
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'payment/payment.html'
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }


    return render(request, template, context)


