from django.shortcuts import render
from .models import Review

def add_review(request):
    """ Display the Add Review form """
    return render(request, 'reviews/add_review.html')


def reviews(request):
    """ Display the Add Review form """
    return render(request, 'reviews/reviews.html')