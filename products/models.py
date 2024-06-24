from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Category(models.Model):

    class Meta:
        """ Fix plural name bug """
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    friendly_name_plural = models.CharField(max_length=254,
                                            null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    product_code = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(
                    validators=[MinValueValidator(Decimal('0.01'))],
                    max_digits=6, decimal_places=2
                    )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
