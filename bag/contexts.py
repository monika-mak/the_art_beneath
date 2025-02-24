from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from art.models import Art


def bag_contents(request):

    bag_items = []
    total = 0
    art_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        art = get_object_or_404(Art, pk=item_id)
        total += item_data * art.price
        art_count += item_data
        bag_items.append({
            'item_id': item_id,
            'quantity': item_data,
            'art': art,
        })

    if total:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
    else:
        delivery = 0

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'art_count': art_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
