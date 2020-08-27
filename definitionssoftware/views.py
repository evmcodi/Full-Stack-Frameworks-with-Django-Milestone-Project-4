from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.template.loader import render_to_string

from definitionssoftware.forms import TermForm
from definitionssoftware.models import Term

from django.contrib.auth.decorators import permission_required, login_required


@login_required
# @permission_required('definitionssoftware.access_paid_definitions_app', raise_exception=True)
# @permission_required('definitionssoftware.access_paid_definitions_app')
def view_definitionssoftware(request):
    """ A view that renders the definitions software template """

    user = request.user

    # Retrieve only the current user's terms.
    terms = Term.objects.filter(user=user)

    template = 'definitionssoftware/definitionssoftware.html'

    context = {
        'terms': terms
    }

    if user.has_perm('definitionssoftware.access_paid_definitions_app'):
        return render(request, template, context)

    return redirect(reverse('payment'))


def save_term_form(request, form, template_name):
    data = dict()

    user = request.user

    if request.method == 'POST':
        if form.is_valid():

            # Save the submitted form to the db, while first programmatically setting
            # the 'user' field to the logged-in user.
            new_term = form.save(commit=False)
            new_term.user = user
            new_term.save()

            # Set the form valid in the response.
            data['form_is_valid'] = True

            # Retrieve only the current user's terms.
            terms = Term.objects.filter(user=user)

            data['html_term_list'] = render_to_string('definitionssoftware/includes/partial_term_list.html', {
                'terms': terms
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def term_create(request):
    if request.method == 'POST':
        form = TermForm(request.POST)
    else:
        form = TermForm()
    return save_term_form(request, form, 'definitionssoftware/includes/partial_term_create.html')
