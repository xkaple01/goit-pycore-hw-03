import mesop as me
from backend.task_3 import get_normalized_phone_number


@me.stateclass
class State:
    input_phone_number: str = ''
    normalization_result: str = ''

def on_load_page_3(e: me.LoadEvent) -> None:
    me.set_theme_mode(theme_mode='light')

def on_click_nav_3(e: me.ClickEvent) -> None:
    me.navigate('/task_3')

def on_input_phone_number(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    state.input_phone_number = e.value

def on_click_button_normalize(e: me.ClickEvent) -> None:
    state: State = me.state(state=State)
    state.normalization_result = get_normalized_phone_number(input_phone_number=state.input_phone_number)

def body_container_3():
    with me.box(style=me.Style(padding=me.Padding(left='2%', right='2%'))):
        task_container()
        with me.box(style=me.Style(display='flex', flex_direction='row', gap='5%', padding=me.Padding(top='16px'))):
            input_container()
            compute_container()
            result_container()

def task_container():
    with me.box(style=me.Style(padding=me.Padding(top='48px', bottom='16px'))):
        me.text(text='Normalize the phone number.')

def input_container():
    with me.box(style=me.Style(width='30%', padding=me.Padding(top='16px'))):
        me.text(text='Enter the phone number:')
        me.input(label='number', on_input=on_input_phone_number, appearance='outline', style=me.Style(padding=me.Padding(top='8px', bottom='8px')))

def compute_container():
    with me.box(style=me.Style(width='30%', text_align='center', padding=me.Padding(top='48px'))):
        me.button(label='Normalize', on_click=on_click_button_normalize, type='stroked')

def result_container():
    state: State = me.state(state=State)
    with me.box(style=me.Style(width='30%', padding=me.Padding(top='24px'))):
        me.text(text='Normalized phone number:')
        me.text(text=f'{state.normalization_result}', style=me.Style(padding=me.Padding(top='20px')))