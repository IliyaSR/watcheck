from django.core.exceptions import ValidationError


def only_letters_name(word):
    for letter in word:
        if not letter.isalpha():
            raise ValidationError('Your name should contain only letters!')


def only_letters_town(town):
    for letter in town:
        if not letter.isalpha():
            raise ValidationError('Your town should contain only letters!')
