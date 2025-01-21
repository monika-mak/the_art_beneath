from django.shortcuts import render
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
