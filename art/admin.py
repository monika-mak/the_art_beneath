from django.contrib import admin
from .models import Art, Category, Specification

# Register your models here.

class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )

class SpecificationAdmin(admin.ModelAdmin):
    list_display = (
        'art',
        'format',
        'size',
    )

admin.site.register(Art, ArtAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Specification, SpecificationAdmin)