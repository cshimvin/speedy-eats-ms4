from django import forms
from .models import Order


# Class taken from Code Institute Course Boutique Ado walkthrough
class OrderForm(forms.ModelForm):
    """ Order form model """
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2', 'town_or_city',
                  'county', 'postcode',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        Remove auto-generated labels.
        Set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        # Create dictionary of placeholders
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        # Set autofocus to Full Name field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        # Add placeholders with set above together with an asterisk
        # if a required field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Style form
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            # Remove form labels
            self.fields[field].label = False
