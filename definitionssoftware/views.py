from django.contrib.auth.models import User
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from definitionssoftware.models import Term

from django.contrib.auth.decorators import permission_required, login_required


@login_required
# @permission_required('definitionssoftware.access_paid_definitions_app', raise_exception=True)
# @permission_required('definitionssoftware.access_paid_definitions_app')
def view_definitionssoftware(request):
    """ A view that renders the definitions software template """

    user = request.user

    terms = Term.objects.all()

    template = 'definitionssoftware/definitionssoftware.html'
    
    context = {
        'terms': terms
    }

    if user.has_perm('definitionssoftware.access_paid_definitions_app'):
        return render(request, template, context)

    return redirect(reverse('payment'))


