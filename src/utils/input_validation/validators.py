import os, sys, uuid 

def validate_room_number(person_id: str) -> bool: 
    """
    Check if the user input for room entity is valid
    """
    if person_id.isnumeric():
        return 0 <= int(person_id) <= 9999
    return False


def validate_guest_id(person_id: str) -> bool:
    """
    Check if the user input for guest entity is valid.
    Return proper exit code for special user id's
    """

    if person_id.isnumeric():
        return "0" <= person_id <= "9999"
    return False


def validate_credit_card_number(credit_card_number: float) -> bool:
    """
    Check if the user input for credit card
        follows the international card standards.
    """
    if credit_card_number.isnumeric():
        return 8 <= len(credit_card_number) <= 19
    return False


def is_phone_number_valid(phone_number: str):
    "Check if the user input for phone number is valid"
    if phone_number.isnumeric():
        return 7 <= len(phone_number) <= 15
    return False

def validate_guest_personal_id(
    guest_personal_id: str,
    guest_country_code: str,
    guest_gender: str,
    guest_birth_year: str,
    guest_birth_mobth: str,
    guest_birth_day: str) -> bool:
    """
    Check if the entered personal_id card number
        follows the EU standards
    """

    if guest_country_code == "LT":
        if guest_personal_id.isnumeric() and len(guest_personal_id) == 1:
            if (guest_gender == "male" and guest_personal_id[0] == '5') or (guest_gender == "female" and not guest_personal_id[0] == '4'):
                if guest_personal_id[1:3] == guest_birth_year[-2:]:
                    if guest_personal_id[3:5] == guest_birth_mobth:
                        if guest_personal_id[6:8] == guest_birth_day:
                            return True
        return False

    if guest_country_code == "BE":
        print("Not implemented")
        return False

    if guest_country_code == "BG":
        print("Not implemented")
        return False

    if guest_country_code == "CZ":
        print("Not implemented")
        return False

    if guest_country_code == "DK":
        print("Not implemented")
        return False

    if guest_country_code == "DE":
        print("Not implemented")
        return False

    if guest_country_code == "EE":
        print("Not implemented")
        return False

    if guest_country_code == "IE":
        print("Not implemented")
        return False

    if guest_country_code == "EL":
        print("Not implemented")
        return False

    if guest_country_code == "ES":
        print("Not implemented")
        return False

    if guest_country_code == "FR":
        print("Not implemented")
        return False

    if guest_country_code == "BE":
        print("Not implemented")
        return False

    if guest_country_code == "HR":
        print("Not implemented")
        return False

    if guest_country_code == "IT":
        print("Not implemented")
        return False

    if guest_country_code == "CY":
        print("Not implemented")
        return False

    if guest_country_code == "LV":
        print("Not implemented")
        return False

    if guest_country_code == "LT":
        print("Not implemented")
        return False

    if guest_country_code == "LU":
        print("Not implemented")
        return False

    if guest_country_code == "HU":
        print("Not implemented")
        return False

    if guest_country_code == "MT":
        print("Not implemented")
        return False

    if guest_country_code == "NL":
        print("Not implemented")
        return False

    if guest_country_code == "AT":
        print("Not implemented")
        return False

    if guest_country_code == "PL":
        print("Not implemented")
        return False

    if guest_country_code == "PT":
        print("Not implemented")
        return False

    if guest_country_code == "RO":
        print("Not implemented")
        return False

    if guest_country_code == "SI":
        print("Not implemented")
        return False

    if guest_country_code == "SK":
        print("Not implemented")
        return False

    if guest_country_code == "FI":
        print("Not implemented")
        return False

    if guest_country_code == "SE":
        print("Not implemented")
        return False

def generate_random_username() -> str:
    """
    Generates a random UIID4 string as a username
    Should be used as temp logic credentials
    """
    return str(uuid.uuid4())
