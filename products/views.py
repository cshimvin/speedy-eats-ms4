from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """ A view to show all food items, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    friendly_name_plural = None

    if request.GET:
        # Get category if category selected
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
            friendly_name_plural = categories[0].friendly_name_plural

        # Get query if a search term has been submitted
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                messages.error(request,
                               "No search criteria have been entered.")
                return redirect(reverse('products'))
            queries = Q(name__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'friendly_name_plural': friendly_name_plural,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show details of a specific food item """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
