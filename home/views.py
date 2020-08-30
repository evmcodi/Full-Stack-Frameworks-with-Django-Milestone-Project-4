from django.shortcuts import render, redirect
from django.contrib.auth.models import Permission
from django.urls import reverse


def index(request):
    """ A view to return the index page """

    user = request.user

    # Check if user has already logged in and redirect to the payment page if unpaid or to definitions app if paid.
    if user.is_authenticated:

        # Check if user has already paid and redirect them to definitions app.
        if user.has_perm('definitionssoftware.access_paid_definitions_app'):
            return redirect(reverse('view_definitionssoftware'))

        return redirect(reverse('payment'))

    return render(request, 'home/index.html')

