from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReviewForm


@login_required
def add_review(request):
    """ Display the Add Review form """

    # Handle form submission
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Review submitted')
        else:
            messages.error(request, 'Review not submitted. \
                Please check your form has been completed correctly.')
    else:
        form = ReviewForm()

    template = 'reviews/add_review.html'
    context = {
        'form': form,
        'no_bag': True,
    }

    return render(request, template, context)


def reviews(request):
    """ Display the Reviews """
    return render(request, 'reviews/reviews.html')
