import re
from enum import Enum
from datetime import datetime, date, timedelta


class Weekday(Enum):
    Monday = 0
    Tuesday = 1
    Wednesday = 2
    Thursday = 3
    Friday = 4
    Saturday = 5
    Sunday = 6

date_format: str = '%Y.%m.%d'

database_employees: list[dict] = []

def convert_string_to_date(date_string: str) -> date:
    return datetime.strptime(date_string, date_format).date()

def convert_date_to_string(orig_date: date) -> str:
    return datetime.strftime(orig_date, date_format)

def convert_date_to_weekday(orig_date: date) -> Weekday:
    return Weekday(value=orig_date.weekday())

def get_interval_start_date() -> str:
    start_date: date = datetime.today().date()
    start_date: str = convert_date_to_string(orig_date=start_date)

    return start_date

def get_interval_end_date(start_date: str) -> str:
    start_date: date = convert_string_to_date(date_string=start_date)
    end_date: date = start_date + timedelta(weeks=1)
    end_date: date = shift_date_if_weekend(orig_date=end_date)

    return datetime.strftime(end_date, date_format)

def check_is_name_input_valid(name_input: str) -> bool:
    return re.fullmatch(pattern='[A-Z]{1}[a-z]{1,15}', string=name_input) is not None

def check_is_date_input_valid(date_input: str) -> bool:
    is_date_input_valid: bool = True
    try:
        convert_string_to_date(date_string=date_input)
    except Exception:
        is_date_input_valid: bool = False

    return is_date_input_valid

def shift_date_if_weekend(orig_date: date) -> date:
    orig_weekday: Weekday = convert_date_to_weekday(orig_date=orig_date)

    if orig_weekday is Weekday.Saturday:
        shifted_date: date = orig_date + timedelta(days=2)
    elif orig_weekday is Weekday.Sunday:
        shifted_date: date = orig_date + timedelta(days=1)
    else:
        shifted_date: date = orig_date

    return shifted_date

def get_total_number_of_employees() -> int:
    return len(database_employees)

def add_eployee_to_database(first_name: str, last_name: str, birthday: str) -> None:
    employee: dict = {'name': f'{first_name} {last_name}', 'birthday': birthday}
    if employee not in database_employees:
        database_employees.append(employee)

def remove_employee_from_database(first_name: str, last_name: str, birthday: str) -> None:
    employee: dict = {'name': f'{first_name} {last_name}', 'birthday': birthday}
    if employee in database_employees:
        database_employees.remove(employee)

def get_all_employees() -> list[dict]:
    return database_employees

def get_upcoming_birthdays(interval_start: str, interval_end: str) -> list[dict]:
    interval_start: date = convert_string_to_date(date_string=interval_start)
    interval_end: date = convert_string_to_date(date_string=interval_end)
    
    employees_to_congratulate: list[dict] = []
    for employee in database_employees:
        birthday: date = convert_string_to_date(date_string=employee['birthday'])
        birthday_this_year: date = birthday.replace(year=datetime.today().date().year)

        if interval_start <= birthday_this_year and birthday_this_year <= interval_end:
            shifted_birthday: date = shift_date_if_weekend(orig_date=birthday_this_year)
            congrat_date_string: str = convert_date_to_string(orig_date=shifted_birthday)

            employees_to_congratulate.append(
                {
                    'name': employee['name'],
                    'birthday': employee['birthday'],
                    'congratulation_date': congrat_date_string
                }
            )

    return employees_to_congratulate