from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Driver


def all_drivers(request):
    """
    A view to show all delivery drivers
    """
    staff = Driver.objects.all()
    context = {
        'staff': staff,
    }
    return render(request, 'staff/drivers.html', context)
