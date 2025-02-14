from django.db import models


class Category(models.Model):
    # override default plural naming in admin panel
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    display_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def get_display_name(self):
        return self.display_name

class Art(models.Model):

    class Meta:
        verbose_name_plural = 'Art'

    # code used from https://docs.djangoproject.com/en/5.1/ref/models/fields/#choices
    ORIENTATION_CHOICES = [
        ('horizontal', 'Horizontal'),
        ('vertical', 'Vertical'),
        ('square', 'Square'),
    ]

    SIZE_CHOICES = [
        ('140x140cm', '140x140cm'),
        ('100x200cm', '100x200cm'),
        ('100x150cm', '100x150cm'),
    ]

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    meaning = models.TextField()
    color = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=0)
    date = models.DateTimeField(auto_now_add=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_2_url= models.URLField(max_length=1024, null=True, blank=True)
    image_2 = models.ImageField(null=True, blank=True)
    orientation = models.CharField(
        max_length=25,
        choices=ORIENTATION_CHOICES, default='square')
    size = models.CharField(
        max_length=25,
        choices=SIZE_CHOICES, default='140x140cm'
        )

    def __str__(self):
        return self.name





