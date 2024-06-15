from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Review form model """
    class Meta:
        model = Review
        fields = ("review_title", "review_body", "rating", "reviewer_name")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'Title of your review',
            'review_body': 'Your review',
            'rating': 'Rating (0-5)',
            'reviewer_name': "Your name",
        }
        self.fields['review_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            # Style form
            self.fields[field].widget.attrs['class'] = 'review-form-input'
            # Remove form labels
            self.fields[field].label = False
