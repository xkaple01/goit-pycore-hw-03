import mesop as me
from backend.task_2 import (
    check_is_input_integer,
    convert_valid_str_to_int,
    check_is_value_within_allowed_interval,
    generate_ticket
)


@me.stateclass
class State:
    quantity_input: str = ''
    quantity_low: int = 1
    quantity_high: int = 10
    is_quantity_input_integer: bool = False
    is_quantity_within_interval: bool = False
    is_quantity_valid: bool = False
    
    min_input: str = ''
    min_low: int = 1
    min_high: int = 999
    is_min_input_integer: bool = False
    is_min_within_interval: bool = False
    is_min_valid: bool = False

    max_input: str = ''
    max_low: int = 2
    max_high: int = 1000
    is_max_input_integer: bool = False
    is_max_within_interval: bool = False
    is_max_valid: bool = False

    lottery_ticket: str = ''

def on_load_page_2(e: me.LoadEvent) -> None:
    me.set_theme_mode(theme_mode='light')

def on_click_nav_2(e: me.ClickEvent) -> None:
    me.navigate('/task_2')

def on_input_quantity(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    state.quantity_input = e.value

    state.is_quantity_valid = False
    state.is_quantity_input_integer = check_is_input_integer(input_value=state.quantity_input)

    if state.is_quantity_input_integer:
        quantity_value: int = convert_valid_str_to_int(input_value=state.quantity_input)
        
        state.is_quantity_within_interval = check_is_value_within_allowed_interval(
            value=quantity_value, low=state.quantity_low, high=state.quantity_high
        )
    
        if state.is_quantity_within_interval:
            state.is_quantity_valid = True
            state.min_high = state.max_high - quantity_value + 1

            on_input_min(e=me.InputEvent(value=state.min_input, key=e.key))
            
def on_input_min(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    state.min_input = e.value
    
    state.is_min_valid = False
    state.is_min_input_integer = check_is_input_integer(input_value=state.min_input)

    if state.is_min_input_integer:
        min_value: int = convert_valid_str_to_int(input_value=state.min_input)

        state.is_min_within_interval = check_is_value_within_allowed_interval(
            value=min_value, low=state.min_low, high=state.min_high
        )

        if state.is_min_within_interval:
            state.is_min_valid = True

            quantity_value: int = convert_valid_str_to_int(input_value=state.quantity_input)
            state.max_low = min_value + quantity_value - 1

            on_input_max(e=me.InputEvent(value=state.max_input, key=e.key))

def on_input_max(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    state.max_input = e.value
    
    state.is_max_valid = False
    state.is_max_input_integer = check_is_input_integer(input_value=state.max_input)
    
    if state.is_max_input_integer:
        max_value: int = convert_valid_str_to_int(input_value=state.max_input)

        state.is_max_within_interval = check_is_value_within_allowed_interval(
            value=max_value, low=state.max_low, high=state.max_high
        )

        if state.is_max_within_interval:
            state.is_max_valid = True

def on_click_generate_button(e: me.ClickEvent) -> None:
    state: State = me.state(state=State)
    state.lottery_ticket = generate_ticket(
        min_input=state.min_input, max_input=state.max_input, quantity_input=state.quantity_input
    )

def get_hint_input_quantity() -> str:
    state: State = me.state(state=State)
    return 'Format is correct' if state.is_quantity_valid else 'Please, provide the value within required range'

def get_hint_input_min() -> str:
    state: State = me.state(state=State)
    return 'Format is correct' if state.is_min_valid else 'Please, provide the value within required range'

def get_hint_input_max() -> str:
    state: State = me.state(state=State)
    return 'Format is correct' if state.is_max_valid else 'Please, provide the value within required range'

def check_is_input_min_disabled() -> bool:
    state: State = me.state(state=State)
    return not state.is_quantity_valid

def check_is_input_max_disabled() -> bool:
    state: State = me.state(state=State)
    return not (state.is_quantity_valid and state.is_min_valid)

def check_is_generate_button_disabled() -> bool:
    state: State = me.state(state=State)
    return not (state.is_quantity_valid and state.is_min_valid and state.is_max_valid)

def body_container_2():
    with me.box(style=me.Style(padding=me.Padding(left='2%', right='2%'))):
        task_container()
        input_container()
        compute_container()
        result_container()

def task_container() -> None:
    with me.box():
        me.text(
            text='Generate the lottery ticket.',
            style=me.Style(padding=me.Padding(top='48px', bottom='16px'))
        )

def input_container() -> None:
    with me.box(style=me.Style(display='flex', flex_direction='row', gap='5%')):
        state: State = me.state(state=State)

        with me.box(style=me.Style(width='30%')):
            me.text(text='Length of lottery ticket:', style=me.Style(padding=me.Padding(top='32px', bottom='4px')))
            me.text(text=f'integer in range [{state.quantity_low}; {state.quantity_high}]', style=me.Style(padding=me.Padding(bottom='16px')))
            me.input(
                label=f'quantity', on_input=on_input_quantity, hint_label=get_hint_input_quantity(),
                appearance='outline', style=me.Style(width='100%', border_radius=8, padding=me.Padding(bottom='16px'))   
            )
        
        with me.box(style=me.Style(width='30%')):
            me.text(text='Min possible generated number:', style=me.Style(padding=me.Padding(top='32px', bottom='4px')))
            me.text(text=f'integer in range [{state.min_low}; {state.min_high}]', style=me.Style(padding=me.Padding(bottom='16px')))
            me.input(
                label=f'min', disabled=check_is_input_min_disabled(), on_input=on_input_min, hint_label=get_hint_input_min(),
                appearance='outline', style=me.Style(width='100%', border_radius=8, padding=me.Padding(bottom='16px'))
            )

        with me.box(style=me.Style(width='30%')):
            me.text(text='Max possible generated number:', style=me.Style(padding=me.Padding(top='32px', bottom='4px')))
            me.text(text=f'integer in range [{state.max_low}; {state.max_high}]', style=me.Style(padding=me.Padding(bottom='16px')))
            me.input(
                label=f'max', disabled=check_is_input_max_disabled(), on_input=on_input_max, hint_label=get_hint_input_max(),
                appearance='outline', style=me.Style(width='100%', border_radius=8, padding=me.Padding(bottom='16px'))
            )

def compute_container() -> None:
    state: State = me.state(state=State)
    with me.box(style=me.Style(text_align='center', padding=me.Padding(top='32px', bottom='16px'))):
        me.button(
            label='Generate', on_click=on_click_generate_button, disabled=check_is_generate_button_disabled(),
            type='stroked', style=me.Style(width='25%')
        )

def result_container() -> None:
    state: State = me.state(state=State)
    with me.box(style=me.Style(width='100%', display='flex', flex_direction='row', gap='4%', padding=me.Padding(top='32px', bottom='16px'))):
        me.text(text=f'Lottery ticket: ')
        me.text(text=f'{state.lottery_ticket}', style=me.Style(color='green', font_weight='bold'))