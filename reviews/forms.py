from django import forms


class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes.
        Remove auto-generated labels.
        Set autofocus to first field
        """
        super().__init__(*args, **kwargs)
        # Create dictionary of placeholders
        placeholders = {
            'review_title': 'Review Title',
            'review_body': 'Review',
            'rating': 'Rating (Out of 5)',
            'review_date': 'Date of Experience',
        }

        # Set autofocus to Full Name field
        self.fields['review_title'].widget.attrs['autofocus'] = True

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
