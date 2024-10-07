import random


def check_is_input_integer(input_value: str) -> bool:
    is_input_valid_int: bool = True
    try:
        int(input_value)
    except Exception:
        is_input_valid_int: bool = False

    return is_input_valid_int

def convert_valid_str_to_int(input_value: str) -> int:
    return int(input_value)

def check_is_value_within_allowed_interval(value: int, low: int, high: int) -> bool:    
    return low <= value and value <= high

def generate_ticket(min_input: str, max_input: str, quantity_input: str) -> str:
    numbers: list[int] = get_numbers_ticket(
        min_value=convert_valid_str_to_int(min_input),
        max_value=convert_valid_str_to_int(max_input),
        quantity_value=convert_valid_str_to_int(quantity_input)
    )
    return str(numbers) 

def get_numbers_ticket(min_value: int, max_value: int, quantity_value: int) -> list[int]:
    try:
        numbers: list[int] = sorted(random.sample(population=range(min_value, max_value + 1), k=quantity_value))
    except Exception:
        numbers: list[int] = []

    return numbers