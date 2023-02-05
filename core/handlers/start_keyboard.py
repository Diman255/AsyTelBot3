import asyncio

from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from core.keyboard.keyboart_inl import inlain_keyboart_start_yaroclavl, inlain_keyboart_bot_point,\
    inlain_keyboart_kamenny, inlain_keyboart_seed, inlain_keyboart_chat, inlain_keyboart_kamenny_arrived, \
    inlain_keyboart_seed_arrived
from core.keyboard.keyboart_rep import reply_duty
from core.settings import settings
from core.utils.local_file_obyekt import local_file_obyect_save, local_file_obyect_load


# выполнение команды Start
async def keyboard_start_command(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    await message.answer(text='Доброго Дня!',
                         reply_markup=reply_duty, disable_notification=False)



# ответ на команду Смена Ямал
async def keyboard_start_otvet1(message: Message, bot: Bot):
    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    if message.from_user.id in settings.bots.duty_yaroclavl:
        rty1 = await message.answer(text=f'Доброго Дня!<b> {message.from_user.full_name}</b>, выберете действие',
                                   reply_markup=inlain_keyboart_start_yaroclavl(), disable_notification=False)
    else:
        await message.answer(text=f'{message.from_user.full_name} Вы не входите в группу Смена Ямал. 😎')
    await asyncio.sleep(10)
    # на всякий случай проверяем есть ли еще сообщение
    try:
        await rty1.delete()
    except Exception as e:
        pass


# ответ на команду Дежурный
async def keyboard_start_otvet2(message: Message, bot: Bot):

    await bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    if message.from_user.id in settings.bots.duty_kamenny + settings.bots.duty_seed:
        rty = await message.answer(text=f'Доброго Дня! <b>{message.from_user.full_name}</b>, выберете действие',
                                   reply_markup=inlain_keyboart_bot_point(), disable_notification=False)
    else:
        await message.answer(text=f'{message.from_user.full_name} Вы не входите в группу дежурных. 😎')
    await asyncio.sleep(10)
    # на всякий случай проверяем есть ли еще сообщение
    try:
        await rty.delete()
    except Exception as e:
        pass


# ответ на кнопку - дежурный
async def button_processing_duty(call: CallbackQuery, bot: Bot):

    await bot.send_message(chat_id=call.message.chat.id, text=f'Добрый День!'
                                                              f'\n Сегодня дежурный,'
                                                              f'\n <u><b>{call.from_user.full_name}</b></u>')
    await call.answer()

    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)

# ответ на кнопку - принял
async def button_processing_accepted(call: CallbackQuery, bot: Bot):
    del_message = int(call.message.message_id) - 2
    await bot.send_message(chat_id=call.message.chat.id, text=f'<u><b>{call.from_user.full_name}</b></u>: Принял ',
                           reply_to_message_id=del_message)

    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


# ответ на выбор кнопки выезжаем
async def button_processing_exit(call: CallbackQuery, bot: Bot):

    if call.from_user.id in settings.bots.duty_kamenny:

        zxc = await bot.send_message(chat_id=call.message.chat.id,
                                     text=f'<u><b>{call.from_user.full_name},'
                                          f' куда выезжаем сегодня?</b></u>',
                                     reply_markup=inlain_keyboart_kamenny(), disable_notification=False)
    elif call.from_user.id in settings.bots.duty_seed:
        zxc = await bot.send_message(chat_id=call.message.chat.id,
                                     text=f'<u><b>{call.from_user.full_name},'
                                          f' куда выезжаем сегодня?</b></u>',
                                     reply_markup=inlain_keyboart_seed(), disable_notification=False)
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await asyncio.sleep(10)
    # на всякий случай проверяем есть ли еще сообщение
    try:
        await zxc.delete()
    except Exception as e:
        pass


# Куда выезжаем
async def inl_went(call: CallbackQuery, bot: Bot, ):

    towers = call.data.split('_')[1]
    answer = f'<b>{call.from_user.full_name}</b>:  Выезжаем на {towers}'

    id_user = call.from_user.id
    obyekt = 'None'
    local_file_obyect_save(id_user, obyekt)

    await bot.send_message(chat_id=call.message.chat.id, text=answer)
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)


# Окончание дежурства
async def inl_exit_duty_local(call: CallbackQuery, bot: Bot, ):

    user_id = call.from_user.id
    user = call.from_user.full_name
    text = f'<b> {user}:</b> Выдвигаюсь домой'

    obyekt = 'None_duty'
    id_user = user_id
    local_file_obyect_save(id_user, obyekt)

    await bot.send_message(chat_id=call.message.chat.id, text=text)
    await call.answer()
    await bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        reply_markup=None)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
