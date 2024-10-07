import mesop as me
from backend.task_4 import (
    get_interval_start_date,
    get_interval_end_date,
    check_is_name_input_valid,
    check_is_date_input_valid,
    add_eployee_to_database,
    remove_employee_from_database,
    get_total_number_of_employees,
    get_upcoming_birthdays
)


@me.stateclass
class State:
    congrat_start: str = ''
    congrat_end: str = ''

    first_name: str = ''
    last_name: str = ''
    birthday: str = ''

    is_first_name_valid: bool = False
    is_last_name_valid: bool = False
    is_birthday_valid: bool = False

    max_num_employees_in_db: int = 32
    
def on_load_page_4(e: me.LoadEvent) -> None:
    me.set_theme_mode(theme_mode='light')

    state: State = me.state(state=State)
    state.congrat_start = get_interval_start_date()
    state.congrat_end = get_interval_end_date(start_date=state.congrat_start)

def on_click_nav_4(e: me.ClickEvent) -> None:
    me.navigate('/task_4')

def on_input_first_name(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    first_name_input: str = e.value

    state.is_first_name_valid = check_is_name_input_valid(name_input=first_name_input)
    
    if state.is_first_name_valid:
        state.first_name = first_name_input

def on_input_last_name(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    last_name_input: str = e.value

    state.is_last_name_valid = check_is_name_input_valid(name_input=last_name_input)
    
    if state.is_last_name_valid:
        state.last_name = last_name_input

def on_input_birthday(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    birthday_input: str = e.value

    state.is_birthday_valid = check_is_date_input_valid(date_input=birthday_input)
    
    if state.is_birthday_valid:
        state.birthday = birthday_input

def on_click_add_employee_to_db(e: me.ClickEvent) -> None:
    state: State = me.state(state=State)
    add_eployee_to_database(first_name=state.first_name, last_name=state.last_name, birthday=state.birthday)

def on_click_remove_employee_from_db(e: me.ClickEvent) -> None:
    state: State = me.state(state=State)
    remove_employee_from_database(first_name=state.first_name, last_name=state.last_name, birthday=state.birthday)

def body_container_4():
    with me.box(style=me.Style(padding=me.Padding(left='2%', right='2%'))):
        task_container()
        input_container()
        compute_container()
        result_container()

def task_container() -> None:
    with me.box():
        me.text(
            text='Find the employees to congratulate in the upcoming week, taking the weekend shifts into account.',
            style=me.Style(padding=me.Padding(top='48px', bottom='16px'))
        )

def input_container() -> None:
    with me.box(style=me.Style(display='flex', flex_direction='row', gap='5%')):
        state: State = me.state(state=State)

        with me.box(style=me.Style(width='30%')):
            me.text(text='Enter employee first name:', style=me.Style(padding=me.Padding(top='32px', bottom='16px')))
            me.input(
                label='Name', on_input=on_input_first_name, appearance='outline',
                style=me.Style(width='100%', border_radius=8, padding=me.Padding(bottom='16px')),
                hint_label='Format is correct' if state.is_first_name_valid else 'Please, provide the first name in the correct format'
            )

        with me.box(style=me.Style(width='30%')):
            me.text(text='Enter employee last name:', style=me.Style(padding=me.Padding(top='32px', bottom='16px')))
            me.input(
                label='Surname', disabled=(not state.is_first_name_valid), on_input=on_input_last_name, appearance='outline',
                style=me.Style(width='100%', border_radius=8, padding=me.Padding(bottom='16px')),
                hint_label='Format is correct' if state.is_last_name_valid else 'Please, provide the last name in the correct format'
            )

        with me.box(style=me.Style(width='30%')):
            me.text(text='Enter employee birthday:', style=me.Style(padding=me.Padding(top='32px', bottom='16px')))
            me.input(
                label='yyyy.mm.dd', disabled=(not (state.is_first_name_valid and state.is_last_name_valid)), on_input=on_input_birthday, appearance='outline',
                style=me.Style(width='100%', border_radius=8, padding=me.Padding(bottom='16px')),
                hint_label='Format is correct' if state.is_birthday_valid else 'Please, provide the date in the correct format'
            )

def compute_container() -> None:
    state: State = me.state(state=State)

    with me.box(style=me.Style(display='flex', flex_direction='row', padding=me.Padding(top='32px', bottom='32px'))):
        with me.box(style=me.Style(width='50%', text_align='center')):
            me.button(
                label='Add to database', on_click=on_click_add_employee_to_db, type='stroked',
                disabled=(not (
                    state.is_first_name_valid and state.is_last_name_valid and state.is_birthday_valid
                    and get_total_number_of_employees() < state.max_num_employees_in_db)
                )
            )

        with me.box(style=me.Style(width='50%', text_align='center')):
            me.button(
                label='Remove from database', on_click=on_click_remove_employee_from_db, type='stroked',
                disabled=(not (state.is_first_name_valid and state.is_last_name_valid and state.is_birthday_valid))
            )

def result_container() -> None:
    state: State = me.state(state=State)
    
    with me.box(style=me.Style(padding=me.Padding(top='16px', bottom='32px'))):
        me.text(text=f'Employees to congratulate: from {state.congrat_start} to {state.congrat_end}:')
    
    with me.box():
        with me.box(style=me.Style(width='100%', display='flex', flex_direction='row', gap='5%')):
            with me.box(style=me.Style(width='30%', font_weight='bold', padding=me.Padding(bottom='8px'))):
                me.text(text='Name')
            with me.box(style=me.Style(width='30%', font_weight='bold', padding=me.Padding(bottom='8px'))):
                me.text(text='Birthday')
            with me.box(style=me.Style(width='30%', font_weight='bold', padding=me.Padding(bottom='8px'))):
                me.text(text='Congratulation Date')

        employees_to_congratulate: list[dict] = get_upcoming_birthdays(
            interval_start=state.congrat_start, interval_end=state.congrat_end
        )

        for employee in employees_to_congratulate:
            with me.box(style=me.Style(width='100%', display='flex', flex_direction='row', gap='5%')):
                with me.box(style=me.Style(width='30%', padding=me.Padding(top='4px', bottom='4px'))):
                    me.text(text=f"{employee['name']}")
                with me.box(style=me.Style(width='30%', padding=me.Padding(top='4px', bottom='4px'))):
                    me.text(text=f"{employee['birthday']}")
                with me.box(style=me.Style(width='30%', padding=me.Padding(top='4px', bottom='4px'))):
                    me.text(text=f"{employee['congratulation_date']}")