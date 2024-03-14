from django import forms

from watcheck.watch.models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text_review']
        widgets = {
            'text_review': forms.Textarea(
                attrs={'class': 'review-text', 'rows': 10, 'cols': 60}
            )
        }
