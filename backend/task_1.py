from datetime import datetime, date, timedelta


date_format: str = '%Y.%m.%d'

def convert_string_to_date(date_string: str) -> date:
    return datetime.strptime(date_string, date_format).date()

def convert_date_to_string(orig_date: date) -> str:
    return datetime.strftime(orig_date, date_format)

def get_current_date() -> date:
    return datetime.today().date()

def get_current_date_string() -> str:
    current_date: date = get_current_date()
    current_date: str = convert_date_to_string(orig_date=current_date)

    return current_date

def check_is_date_valid(target_date: str) -> bool:
    is_date_format_correct: bool = True
    try:
        convert_string_to_date(date_string=target_date)
    except Exception:
        is_date_format_correct: bool = False

    return is_date_format_correct

def get_num_days(target_date: str) -> str:
    return str(get_days_from_today(target_date=target_date))

def get_days_from_today(target_date: str) -> int:
    current_date: date = get_current_date()
    target_date: date = convert_string_to_date(date_string=target_date)

    td: timedelta = target_date - current_date
    num_days: int = td.days

    return num_days