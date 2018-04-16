from django.core.exceptions import ValidationError


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            ('%(value)s is not an even number'),
            params={'value': value},
        )


def validate_email(value):
    email = value
    if ".edu" in email:
        raise ValidationError("Nota accept edu")


CATEGORY_LIST = ['Mexican', 'Polish', 'American', 'Asian']


def validate_category(value):
    cat = value.capitalize
    if not value in CATEGORY_LIST and not cat in CATEGORY_LIST:
        raise ValidationError("Ta kategoria jest niedozwolona")