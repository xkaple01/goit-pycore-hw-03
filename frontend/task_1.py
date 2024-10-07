import mesop as me
from backend.task_1 import get_current_date_string, check_is_date_valid, get_num_days


@me.stateclass
class State:
    current_date: str = ''
    target_date: str = ''
    is_date_format_correct: bool = False
    num_days: str = ''

def on_load_page_1(e: me.LoadEvent) -> None:
    me.set_theme_mode(theme_mode='light')
    state: State = me.state(state=State)
    state.current_date = get_current_date_string()

def on_click_nav_1(e: me.ClickEvent) -> None:
    me.navigate('/task_1')

def on_input_target_date(e: me.InputEvent) -> None:
    state: State = me.state(state=State)
    state.target_date = e.value
    state.is_date_format_correct = check_is_date_valid(target_date=state.target_date)

def on_click_compute_button(e: me.ClickEvent) -> None:
    state: State = me.state(state=State)
    state.num_days = get_num_days(target_date=state.target_date)

def body_container_1() -> None:
    with me.box(style=me.Style(padding=me.Padding(left='2%', right='2%'))):
        task_container()
        input_container()
        compute_container()
        result_container()

def task_container() -> None:
    with me.box():
        me.text(
            text='Compute the number of days between the current date and the target date.',
            style=me.Style(padding=me.Padding(top='48px', bottom='16px'))
        )

def input_container() -> None:
    with me.box(style=me.Style(display='flex', flex_direction='row', gap='4%')):
        state: State = me.state(state=State)

        with me.box(style=me.Style(width='50%')):
            me.text(text='Current date is:', style=me.Style(padding=me.Padding(top='32px', bottom='16px')))
            me.input(label=f'{state.current_date}', disabled=True, appearance='outline', style=me.Style(width='100%', border_radius=8))

        with me.box(style=me.Style(width='50%')):
            me.text(text='Enter the target date:', style=me.Style(padding=me.Padding(top='32px', bottom='16px')))
            me.input(
                label='yyyy.mm.dd', on_input=on_input_target_date, appearance='outline', style=me.Style(width='100%', border_radius=8),
                hint_label='Date format is correct' if state.is_date_format_correct else 'Please, provide the date in the correct format'
            )

def compute_container() -> None:
    state: State = me.state(state=State)
    with me.box(style=me.Style(text_align='center', padding=me.Padding(top='32px', bottom='16px'))):
        me.button(
            label='Compute', on_click=on_click_compute_button, type='stroked', style=me.Style(width='25%'),
            disabled=True if not state.is_date_format_correct else False
        )

def result_container() -> None:
    state: State = me.state(state=State)
    with me.box(style=me.Style(width='50%', display='flex', flex_direction='row', gap='4%', padding=me.Padding(top='24px', bottom='16px'))):
        me.text(text=f'Number of days between the dates is:')
        me.text(text=f'{state.num_days}', style=me.Style(color=('green' if len(state.num_days) > 0 and int(state.num_days) > 0 else 'red'), font_weight='bold'))