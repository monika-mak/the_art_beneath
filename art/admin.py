from django.contrib import admin
from .models import Art, Category

# Register your models here.


class ArtAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image',
        'orientation',
        'size',
        'date'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'display_name',
        'name',
    )


admin.site.register(Art, ArtAdmin)
admin.site.register(Category, CategoryAdmin)
