
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from definitionssoftware.models import Term


def view_definitionssoftware(request):
    """ A view that renders the definitions software template """

    return render(request, 'definitionssoftware/definitionssoftware.html')