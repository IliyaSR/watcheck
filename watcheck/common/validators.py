from django.core.exceptions import ValidationError


def only_capital_letters(word):
    for letter in word:
        if letter.isalpha():
            if not letter.isupper():
                raise ValidationError("You should use only capital letters!")
