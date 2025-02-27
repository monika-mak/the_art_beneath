from django.db import models
from art.models import Art


class ContactRequest(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    art = models.ForeignKey(
        Art, on_delete=models.SET_NULL, null=True, blank=True
    )
    message = models.TextField()
    custom_size = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)


def __str__(self):
    art_title = self.art.title if self.art else "General Inquiry"
    return f"Request from {self.name} for {art_title}"
