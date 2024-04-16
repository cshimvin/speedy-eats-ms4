from django import forms
from .models import Category, Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'name', 'description',
                  'price', 'image_url', 'image',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        # From Code Institute course Boutique Ado walkthrough
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names

