from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Art, Category


# Create your views here.
def all_art(request):
    """
    A view to show all art, including sorting and search queries
    """
    
    art = Art.objects.all()
    query = None
    categories = None


# Cofigure search query 

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            art = art.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('art'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            art = art.filter(queries)

    context = {
        'art' : art,
        'search_term': query,
        'current_categories': categories,

    }

    return render(request, 'art/art.html', context)


# Create your views here.
def art_detail(request, art_id):
    """
    A view to show individual art pieces detail.
    """
    
    art = get_object_or_404(Art, pk=art_id)

    context = {
        'art' : art,
    }

    return render(request, 'art/art_detail.html', context)

