from .field import Field
from exceptions.phone import PhoneException


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not (value.isdigit() and len(value) == 10):
            raise PhoneException('the phone number is invalid')
