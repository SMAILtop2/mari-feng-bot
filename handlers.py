from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
import texts
import keyboards as kb

router = Router()

# Обработка команд
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(texts.START_TEXT, reply_markup=kb.main_menu_kb(), parse_mode="HTML")

@router.message(Command("courses"))
async def cmd_courses(message: Message):
    await message.answer(texts.COURSES_MAIN_TEXT, reply_markup=kb.courses_list_kb(), parse_mode="HTML")

@router.message(Command("calendar"))
async def cmd_calendar(message: Message):
    await message.answer(texts.CALENDAR_TEXT, reply_markup=kb.back_to_main_kb(), parse_mode="HTML")

@router.message(Command("registration"))
async def cmd_registration(message: Message):
    await message.answer(texts.REGISTRATION_TEXT, reply_markup=kb.courses_list_kb(), parse_mode="HTML")

@router.message(Command("fs1"))
async def cmd_fs1(message: Message):
    await show_course(message, "fs1")

@router.message(Command("fs2"))
async def cmd_fs2(message: Message):
    await show_course(message, "fs2")

@router.callback_query(F.data.startswith("schedule_"))
async def cb_course_schedule(callback: CallbackQuery):
    course_key = callback.data.split("_")[1]
    data = texts.COURSES_DATA[course_key]
    await callback.message.edit_text(
        f"<b>Расписание: {data['title']}</b>\n\n{data['schedule_text']}",
        reply_markup=kb.course_schedule_kb(course_key),
        parse_mode="HTML"
    )

# Обработка Callback-кнопок
@router.callback_query(F.data == "menu_main")
async def cb_main(callback: CallbackQuery):
    await callback.message.edit_text(texts.START_TEXT, reply_markup=kb.main_menu_kb(), parse_mode="HTML")

@router.callback_query(F.data == "menu_courses")
async def cb_courses(callback: CallbackQuery):
    await callback.message.edit_text(texts.COURSES_MAIN_TEXT, reply_markup=kb.courses_list_kb(), parse_mode="HTML")

@router.callback_query(F.data == "menu_calendar")
async def cb_calendar(callback: CallbackQuery):
    # Если перешли из меню, используем edit_text, иначе отправляем новым сообщением
    try:
        await callback.message.edit_text(texts.CALENDAR_TEXT, reply_markup=kb.back_to_main_kb(), parse_mode="HTML")
    except:
        await callback.message.answer(texts.CALENDAR_TEXT, reply_markup=kb.back_to_main_kb(), parse_mode="HTML")
    await callback.answer()

@router.callback_query(F.data == "menu_registration")
async def cb_registration(callback: CallbackQuery):
    await callback.message.edit_text(texts.REGISTRATION_TEXT, reply_markup=kb.courses_list_kb(), parse_mode="HTML")

@router.callback_query(F.data.startswith("course_"))
async def cb_course_detail(callback: CallbackQuery):
    course_key = callback.data.split("_")[1]
    data = texts.COURSES_DATA[course_key]
    await callback.message.edit_text(
        f"<b>{data['title']}</b>\n\n{data['desc']}",
        reply_markup=kb.course_detail_kb(course_key),
        parse_mode="HTML"
    )

@router.callback_query(F.data.startswith("pay_"))
async def cb_pay(callback: CallbackQuery):
    course_key = callback.data.split("_")[1]
    data = texts.COURSES_DATA[course_key]
    await callback.message.edit_text(
        f"Регистрация на: <b>{data['title']}</b>\nК оплате: {data['price_text']}",
        reply_markup=kb.payment_kb(data['link']),
        parse_mode="HTML"
    )

async def show_course(message: Message, course_key: str):
    data = texts.COURSES_DATA[course_key]
    await message.answer(
        f"<b>{data['title']}</b>\n\n{data['desc']}",
        reply_markup=kb.course_detail_kb(course_key),
        parse_mode="HTML"
    )