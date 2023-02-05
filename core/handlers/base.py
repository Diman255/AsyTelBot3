import json
import os

import urllib.request
from aiogram.methods import send_document
from aiogram import Bot
from aiogram.types import Message, InputMediaPhoto, FSInputFile, CallbackQuery, InputFile
import asyncio
from core.utils.coordinat import get_coordinates
#from core.keyboard.keyboart_inl import inlain_keyboart_bot, inlain_keyboart_chat
from core.keyboard.keyboart_rep import keyboard_txt2





#async def get_start(message: Message, bot: Bot):
    #await message.answer(f'Вы писали {message.text}')

    #son_str = json.dumps(message.dict(), default=str)
    #print(son_str)
    #if message.media_group_id != None:
    #sdf=c_group.append(message.photo[-1].file_id)
    #print(c_group, message.photo[-1].file_id)
    #await asyncio.sleep(0)
    #print(c_group, message.photo[-1].file_id)



    #sdf=['AgACAgIAAxkBAAIFDGOajSShU1UpR6myeWC6bUKTbgTeAALgwjEbuv7RSK8Iu6qMfGcRAQADAgADeQADLAQ',
         #'AgACAgIAAxkBAAIFDWOajSTg_b5UlZqaYDBDs1xnFuV9AALhwjEbuv7RSMtNZAL__QVmAQADAgADeQADLAQ']
    #al1 = InputMediaPhoto(types='poto', media=sdf[0])
    #al2 = InputMediaPhoto(types='poto', media=sdf[1])
    #media=[al1]
    #await  bot.send_media_group(chat_id=message.chat.id, media=media)

    #await bot.answer_media_group(media=sdf)
    #await bot.forward_message(chat_id=message.chat.id, from_chat_id=message.from_user.id, message_id=message.message_id)



    # print(message.media_group_id, message.caption)
    #if message.media_group_id != None:
    #    caption_group=message.caption
    #    print(message.media_group_id, caption_group)
    #await bot.copy_message(chat_id=message.chat.id, from_chat_id=message.from_user.id, message_id=message.message_id, caption='чтот не так')

    #await bot.send_message(message.from_user.id, f'Привет я Бот {message.from_user.first_name}')
    #await message.answer(f'Вы писали {message.text}')
    #await message.reply(f'Привет я Бот {message.from_user.full_name}данная команда используется как ответ на сообщение')


# first_name - имя пользователя full_name - полное имя пользователя (имя и фамилия)
# async def get_start_start(message: Message, bot: Bot):

    #await bot.send_message(chat_id=-1001816256857, text=f'{message.from_user.first_name}  Вы вели команду старт')
    #await message.answer(text='возврат', reply_markup=inlain_keyboart_chat())








#async def location(call: CallbackQuery, bot: Bot):
    #print('локация')
    #print(call)

    #await bot.answer_callback_query(callback_query_id=call.id, text='Privet', url='t.me/JymiLov_bot?start=125', )




async def get_start(message: Message, bot: Bot):
    # await message.answer(f'{message.from_user.first_name},  и Вам Привет')
    message_save = [message.from_user.full_name, message.text]

    await bot.send_message(chat_id=message.chat.id, text=message.md_text+f'{message.from_user.full_name} Pад вас видеть')
    print(message.from_user.id, message.from_user.full_name)

    asd = 'archive/archive.zip'
    asd = FSInputFile(asd)
    await bot.send_document(chat_id=-1001816256857, document=asd, disable_content_type_detection=False)



async def get_start_photo(message: Message, bot: Bot):
    #await message.answer(f'{message.from_user.first_name},  Фото получил')
    #json_str=json.dumps(message.dict(), default=str)
    file = await bot.get_file(message.photo[-1].file_id)
    direct = str(file.file_path).split('/')
    if not os.path.isdir(direct[0]):
        os.mkdir(direct[0])

    patch_files = str(file.file_path)
    await bot.download_file(file.file_path, patch_files)
    print(file.file_path)

async def get_start_video(message: Message, bot: Bot):
    await message.answer(f'{message.from_user.first_name},  Видео получил')
    #json_str=json.dumps(message.dict(), default=str)
    file = await bot.get_file(message.video.file_id)
    direct = str(file.file_path).split('/')
    if not os.path.isdir(direct[0]):
        os.mkdir(direct[0])

    patch_files = str(file.file_path)
    await bot.download_file(file.file_path, patch_files)
    print(file.file_path)