from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def add_review(request):
    """ Display the Add Review form """
    return render(request, 'reviews/add_review.html')


def reviews(request):
    """ Display the Add Review form """
    return render(request, 'reviews/reviews.html')
