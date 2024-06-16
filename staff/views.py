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


def edit_driver(request, driver_id):
    """
    A view to edit a driver's details
    """
    # Check user has permission to access the function
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission \
            to access this function.')
        return redirect(reverse('home'))

    driver = get_object_or_404(Driver, pk=driver_id)

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver)
        if form.is_valid():
            form.save()
            messages.success(request, 'Driver details successfully updated.')
        else:
            messages.error(request, 'Driver details update failed. \
                Check your form input and try again.')
    else:
        form = DriverForm(instance=driver)
        messages.info(request, f'You are currently editing \
            {driver.first_name} {driver.last_name}')

    template = 'staff/edit_driver.html'
    context = {
        'form': form,
        'driver': driver,
        'no_bag': True,
    }

    return render(request, template, context)


def driver_detail(request, driver_id):
    """
    A view to show details of a specific food item
    """
    staff = get_object_or_404(Driver, pk=driver_id)
    context = {
        'staff': staff,
    }

    return render(request, 'staff/driver_detail.html', context)


def delete_driver(request, driver_id):
    """
    Delete a driver from the website
    """
    # Check user has permission to access the function
    if not request.user.is_superuser:
        messages.error(request, 'You do not have permission \
            to access this function.')
        return redirect(reverse('home'))

    driver = get_object_or_404(Driver, pk=driver_id)
    driver.delete()
    messages.success(request, 'Driver has been deleted.')
    return redirect(reverse('all_drivers'))
