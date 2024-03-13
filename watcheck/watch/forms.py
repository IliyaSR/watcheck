from django import forms

from watcheck.watch.models import Review


class ReviewForm(forms.Form):
    class Meta:
        model = Review
        fields = ['rating', 'text_review', 'date_post']

