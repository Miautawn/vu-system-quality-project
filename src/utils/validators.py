from typing import Callable, Any, Optional
import re

EMAIL_PATTERN = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

def validate_name(name: str) -> bool:
    if name and not _contains_numbers(name):
        return True
    return False
    
def validate_email(email: str) -> bool:
    return EMAIL_PATTERN.match(email) is not None

def validate_room_key(product_name: str) -> bool:
    return product_name.isdigit()

def validate_phone_number(phone_number: str) -> bool:
    return phone_number.isdigit()

def validate_room_price(price: str) -> bool:
    if _is_float(price):
        if float(price) > 0.0:
            return True
    return False

def _is_float(number: Any) -> bool:
    try:
        float(number)
        return True
    except:
        return False

def _contains_numbers(input):
    return any(char.isdigit() for char in input)
