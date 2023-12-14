from re import match
from django.core.exceptions import ValidationError


def phone_validator(phone_number: str) -> bool:
    pattern = r'^\+?[0-9]{11}$'
    if not match(pattern=pattern, string=phone_number):
        raise ValidationError("Not correct phone number")



