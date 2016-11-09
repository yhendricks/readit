from django import forms
from .models import Book


class ReviewForm(forms.Form):
    """
    Form for reviewing a book
    """

    is_favourite = forms.BooleanField(
        label='Favourite?',
        help_text='In your top 100 book of all time?',
        required=False,
    )

    review = forms.CharField(
        widget=forms.Textarea,
        min_length=300,
        error_messages={
            'required': 'Plese enter your review',
            'min_length': 'Please write at least 300 characters (you have written %(show_value)s)'
        }
    )
