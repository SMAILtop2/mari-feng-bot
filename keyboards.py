from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from texts import COURSES_DATA

def main_menu_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="КУРСЫ", callback_data="menu_courses")
    kb.button(text="РАСПИСАНИЕ", callback_data="menu_calendar")
    kb.button(text="ЗАПИСЬ", callback_data="menu_registration")
    kb.adjust(1)
    return kb.as_markup()

def courses_list_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    for key, data in COURSES_DATA.items():
        kb.button(text=data["title"], callback_data=f"course_{key}")
    kb.button(text="🔙 Назад", callback_data="menu_main")
    kb.adjust(1)
    return kb.as_markup()


def course_detail_kb(course_key: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()

    # Если у курса есть индивидуальное расписание, показываем его
    if "schedule_text" in COURSES_DATA[course_key]:
        kb.button(text="🔘 РАСПИСАНИЕ", callback_data=f"schedule_{course_key}")
    # Для остальных курсов (кроме искусства и мандал) кидаем в общее
    elif course_key not in ["art", "mandala"]:
        kb.button(text="🔘 РАСПИСАНИЕ", callback_data="menu_calendar")

    kb.button(text="🔘 ЗАПИСЬ", callback_data=f"pay_{course_key}")
    kb.button(text="🔙 К списку курсов", callback_data="menu_courses")
    kb.adjust(1)
    return kb.as_markup()

def course_schedule_kb(course_key: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🔘 ЗАПИСЬ", callback_data=f"pay_{course_key}")
    kb.button(text="🔙 Назад к курсу", callback_data=f"course_{course_key}")
    kb.adjust(1)
    return kb.as_markup()

def back_to_main_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="🔙 Назад в меню", callback_data="menu_main")
    return kb.as_markup()

def payment_kb(url: str) -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.button(text="💳 Оплатить", url=url)
    kb.button(text="🔙 Назад", callback_data="menu_registration")
    kb.adjust(1)
    return kb.as_markup()