import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from aiogram.types import BotCommand# Настройка логирования
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # Подключаем роутер с обработчиками
    dp.include_router(router)

    # Настраиваем меню команд
    await bot.set_my_commands([
        BotCommand(command="start", description="Главное меню"),
        BotCommand(command="courses", description="Список курсов"),
        BotCommand(command="calendar", description="Расписание"),
        BotCommand(command="registration", description="Запись на курсы")
    ])

    # Запуск поллинга
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")