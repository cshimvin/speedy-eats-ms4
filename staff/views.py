from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Driver
from .forms import DriverForm


def all_drivers(request):
    """
    A view to show all delivery drivers
    """
    staff = Driver.objects.all()
    context = {
        'staff': staff,
    }
    return render(request, 'staff/drivers.html', context)


def add_driver(request):
    """
    A view to add a delivery driver to the site
    """
    # Check user has permission to access the function
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission \
            to access this function.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver added successfully')
            return redirect(reverse('add_driver'))
        else:
            messages.error(request, 'Driver not added. \
                Check your form input and try again')
    else:
        form = DriverForm()

    template = 'staff/add_driver.html'
    context = {
        'form': form,
        'no_bag': True
    }

    return render(request, template, context)
