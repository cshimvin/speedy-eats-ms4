from django.shortcuts import render


def index(request):
    """ Display index page """
    return render(request, 'home/index.html')
