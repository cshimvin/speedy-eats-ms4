from django import forms
from .models import Driver


class DriverForm(forms.ModelForm):
    """ Delivery driver form model """
    class Meta:
        model = Driver
        fields = ('staff_number', 'first_name', 'last_name',
                  'vehicle_type', 'vehicle_reg_number')

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        Remove auto-generated labels.
        Set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        # Create dictionary of placeholders
        placeholders = {
            'staff_number': 'Staff number',
            'first_name': 'First name',
            'last_name': 'Last name',
            'vehicle_type': 'Vehicle type',
            'vehicle_reg_number': 'Vehicle registration number',
        }
        # Set autofocus to Staff number field
        self.fields['staff_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Style form
            self.fields[field].widget.attrs['class'] = 'driver-form-input'
            # Remove form labels
            self.fields[field].label = False
