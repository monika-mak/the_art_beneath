from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist
from art.models import Art


@login_required
def wishlist_view(request):
    # Get or create the wishlist for the current user
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist': wishlist})


@login_required
def add_to_wishlist(request, art_id):
    art = get_object_or_404(Art, id=art_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    messages.info(request, f'Added {art.name} to your wishlist')
    wishlist.items.add(art)
    return redirect('wishlist')


@login_required
def remove_from_wishlist(request, art_id):
    art = get_object_or_404(Art, id=art_id)
    wishlist = get_object_or_404(Wishlist, user=request.user)
    messages.info(request, f'Removed {art.name} from your wishlist')
    wishlist.items.remove(art)
    return redirect('wishlist')
