import re


def get_normalized_phone_number(input_phone_number: str) -> str:
    try:
        result: str = normalize_phone(input_phone_number=input_phone_number)
    except Exception as e:
        result: str = str(e)

    return result

def normalize_phone(input_phone_number: str) -> str:
    digits: str = re.sub(pattern='[^0-9]', repl='', string=input_phone_number)
    num_digits: int = len(digits)

    if num_digits <= 8:
        raise ValueError('must contain more that 8 digits')
    elif num_digits >= 13:
        raise ValueError('must contain less than 13 digits')
    
    normalized_phone_number: str = f'+380{digits[-9:]}'

    return normalized_phone_number