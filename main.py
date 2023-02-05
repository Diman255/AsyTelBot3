import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import InlineQuery
from core.handlers import time_archiv
from core.middleware.contentmiddleware import MediaGroupMiddleware
from core.handlers.albums_save import handle_albums
from core.utils.command import command_shtat
from core.settings import settings
from core.handlers.start_keyboard import keyboard_start_command, button_processing_duty, button_processing_accepted, \
    button_processing_exit, inl_went, keyboard_start_otvet1, keyboard_start_otvet2, inl_exit_duty_local
from core.handlers.iline_regim import location_exit
from core.handlers.save_file import photo_file
from core.handlers import time_archiv
from datetime import datetime, timedelta
from aiogram.filters import Command
from aiogram import F
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram.types import CallbackQuery
from aiogram.utils.keyboard import CallbackData


async def start_bot(bot: Bot):
    await command_shtat(bot)
    # await bot.send_message(settings.bots.admin_id, text='Бот запущен')
    print('Бот запущен')


async def stop_bot(bot: Bot):
    # await bot.send_message(settings.bots.admin_id, text='Бот остановлен')
    print('Бот остановлен')


# Функция запуска бота
async def start():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] -  %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.add_job(time_archiv.timing_archive, trigger='cron', hour=7,
                      minute=0, kwargs={'bot': bot})
    scheduler.start()

    dp.message.middleware.register(MediaGroupMiddleware())
    # зарегистрируем наш хендлер в нашем случае это message c функцией get_start передается только название функции
    # без ()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(keyboard_start_otvet1, F.text == '📡 Смена Ярославль')
    dp.message.register(keyboard_start_otvet2, F.text == '⚒ Дежурный Ямал')
    dp.message.register(handle_albums, F.media_group_id)
    dp.message.register(photo_file, F.photo)
    dp.message.register(photo_file, F.video)
    dp.callback_query.register(inl_went, F.data.startswith('tower_'))
    dp.callback_query.register(button_processing_exit, F.data == 'exit_local')
    dp.callback_query.register(inl_exit_duty_local, F.data == 'exit_duty_local')
    dp.callback_query.register(button_processing_accepted, F.data == 'accepted_yaroclavl')
    dp.callback_query.register(button_processing_duty, F.data == 'duty_yaroclavl')
    dp.inline_query.register(location_exit, F.query == 'location_duty')
    dp.message.register(keyboard_start_command, Command(commands=['start']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
