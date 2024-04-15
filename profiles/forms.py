from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """ Profile form model """
    class Meta:
        model = UserProfile

        # Exclude user field to prevent it being amended
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        Remove auto-generated labels.
        Set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        # Create dictionary of placeholders
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_town_or_city': 'Town or City',
            'default_county': 'County',
            'default_postcode': 'Postal Code',
        }

        # Set autofocus to Full Name field
        self.fields['default_phone_number'].widget.attrs['autofocus'] = True

        # Add placeholders with set above together with an asterisk
        # if a required field
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Style form
            self.fields[field].widget.attrs['class'] = 'profile-form-input'
            # Remove form labels
            self.fields[field].label = False
