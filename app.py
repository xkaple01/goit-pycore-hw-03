import mesop as me
from typing import Callable

from frontend.task_1 import on_load_page_1, on_click_nav_1, body_container_1
from frontend.task_2 import on_load_page_2, on_click_nav_2, body_container_2
from frontend.task_3 import on_load_page_3, on_click_nav_3, body_container_3
from frontend.task_4 import on_load_page_4, on_click_nav_4, body_container_4


security_policy = me.SecurityPolicy(dangerously_disable_trusted_types=True)

@me.page(path='/', title='Main',on_load=on_load_page_1, security_policy=security_policy)
def page_index():
    page_base(body_container=body_container_1)

@me.page(path='/task_1', title='Task 1', on_load=on_load_page_1, security_policy=security_policy)
def page_1():
    page_base(body_container=body_container_1)

@me.page(path='/task_2', title='Task 2', on_load=on_load_page_2, security_policy=security_policy)
def page_2():
    page_base(body_container=body_container_2)

@me.page(path='/task_3', title='Task 3', on_load=on_load_page_3, security_policy=security_policy)
def page_3():
    page_base(body_container=body_container_3)

@me.page(path='/task_4', title='Task 4', on_load=on_load_page_4, security_policy=security_policy)
def page_4():
    page_base(body_container=body_container_4)

def page_base(body_container: Callable[[None], None]) -> None:
    with me.box(style=me.Style(background='#000000', width='100%', height='100%', font_family='Roboto', font_size=14)):
        with me.box(style=me.Style(background='#fbfce6', width='720px', border_radius=8, margin=me.Margin.symmetric(horizontal='auto'))):
            header_menu()
            body_container()
            footer()

def top_nav_button(label: str, width: str, on_click_handler: Callable[[me.ClickEvent], None]) -> None:
    with me.box(style=me.Style(width=width, padding=me.Padding(top='16px', bottom='16px'))):
        me.button(label=label, on_click=on_click_handler)

def header_menu() -> None:
    with me.box(style=me.Style(background='#bfdcff', text_align='center', display='flex', flex_direction='row', border_radius=8)):
        nav_handlers: list[Callable[[me.ClickEvent], None]] = [on_click_nav_1, on_click_nav_2, on_click_nav_3, on_click_nav_4]
        for i, handler in enumerate(nav_handlers):
            top_nav_button(label=f'Task {i + 1}', width=f'{100 // len(nav_handlers)}%', on_click_handler=handler)

def footer() -> None:
    with me.box(style=me.Style(padding=me.Padding(top='16px', bottom='16px'))):
        me.text(text='')