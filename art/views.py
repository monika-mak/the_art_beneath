from django.shortcuts import render, get_object_or_404
from .models import Art


# Create your views here.
def all_art(request):
    """
    A view to show all art, including sorting and search queries
    """
    
    art = Art.objects.all()

    context = {
        'art' : art,
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

