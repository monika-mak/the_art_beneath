from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import ContactRequest

@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "art", "custom_size", "created_at", "responded")
    list_filter = ("responded", "created_at")
    search_fields = ("name", "email", "art__title")

    def mark_as_responded(self, request, queryset):
        queryset.update(responded=True)

    actions = [mark_as_responded]