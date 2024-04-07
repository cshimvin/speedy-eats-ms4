from django.shortcuts import render


def view_bag(request):
    """ Display the contents of the shopping bag """
    return render(request, 'bag/bag.html')
