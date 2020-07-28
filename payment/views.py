from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


@login_required
def view_payment(request):
    """ A view that renders the payment page template """

    user = request.user

    # Check if user has already paid and redirect them to definitions app.
    if user.has_perm('definitionssoftware.access_paid_definitions_app'):
        return redirect(reverse('view_definitionssoftware'))

    return render(request, 'payment/payment.html')

