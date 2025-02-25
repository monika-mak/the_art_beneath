from django.db import models
from django.contrib.auth.models import User
from art.models import Art


class Wishlist(models.Model):
    '''
    A model to represent a wishlist
    '''
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wishlist')
    items = models.ManyToManyField(Art, blank=True, related_name='wishlisted_by')

    def __str__(self):
        return f"{self.user.username}'s Wishlist"