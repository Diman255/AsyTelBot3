import os
from typing import List
from aiogram import Bot
from aiogram.types import (
    InputMediaAudio,
    InputMediaDocument,
    InputMediaPhoto,
    InputMediaVideo,
    Message,
)
from core.utils.jymal_obyect import save_obyect_jymal
from core.utils.local_file_obyekt import local_file_obyect_load
from core.settings import settings


def caption_element_album(caption, user_file, user_id):
    save_file_obyect = local_file_obyect_load()
    print(save_file_obyect)
    if caption == 'None':
        text = '😡 Файл отправлен в общую папку - None'
        captions = 'None' + ' ' + user_file
        caption_dir = captions.split(' ')

        for key, value in save_file_obyect.items():

            if key == user_id and save_file_obyect[key] != 'None':
                captions = save_file_obyect[key] + ' ' + user_file
                caption_dir = captions.split(' ')
                print(caption_dir)
                text = 'None'
            if key == user_id and save_file_obyect[key] == 'None_duty':
                text = 'Ignor'

    if caption != 'None':
        captions = caption.capitalize()  # делаем первый символ заглавным
        caption_dir = captions.split(' ')
        tower_jymal = save_obyect_jymal()
        text = 'None'
        if caption == '👍':
            text = 'Ignor'
        # проверка объекта
        elif caption_dir[0] not in tower_jymal:

            text = '😡 Файл отправлен в общую папку - None'
            captions = caption + '_' + user_file
            caption_dir = ['None']

            for key, value in save_file_obyect.items():

                if key == user_id and save_file_obyect[key] != 'None' and save_file_obyect[key] != 'None_duty':
                    captions = save_file_obyect[key] + ' ' + caption
                    caption_dir = captions.split(' ')
                    print(caption_dir)
                    text = 'None'

    result_caption_element = [captions, caption_dir, text]
    return result_caption_element


def save_element_album(file, caption, caption_dir, date):
    file_patch = str(file.file_path).split('/')

    # save/obyekt/data/caption+patch_files
    direct_photo_file = str(' save/' + caption_dir[0] + '/' + date[0] + '/' + caption + '_' + file_patch[1])

    direct_photo = str(' save/' + caption_dir[0] + '/' + date[0])

    print(direct_photo_file, direct_photo)

    if not os.path.isdir(direct_photo):
        os.makedirs(direct_photo)

    save_element = [file.file_path, direct_photo_file]
    return save_element


async def handle_albums(message: Message, bot: Bot, album: List[Message]):
    # async def handle_albums(message: Message, bot: Bot):
    """This handler will receive a complete album of any type."""

    if message.from_user.id in settings.bots.duty_kamenny + settings.bots.duty_seed:
        dates = str(message.date).split(' ')
        # await message.answer(f'Вы писали {album}')

        captionst = 'None'
        for element in album:
            caption = str(element.caption)

            if caption != 'None':
                captionst = caption
        caption = captionst

        print(caption)

        user_file = str(message.from_user.full_name)
        user_id = str(message.from_user.id)

        caption_element = caption_element_album(caption, user_file, user_id)  # проверяем подпись по фото
        captions = caption_element[0]
        caption_dir = caption_element[1]
        if caption_element[2] != 'Ignor':
            if caption_element[2] != 'None':
                await message.answer(text=caption_element[2])

            for element in album:

                if element.photo:
                    file = await bot.get_file(element.photo[-1].file_id)

                    # input_media = InputMediaPhoto(media=element.photo[-1].file_id, **caption_kwargs)
                elif element.video:
                    file = await bot.get_file(element.video.file_id)

                    # input_media = InputMediaVideo(media=element.video.file_id, **caption_kwargs)

                else:
                    pass
                save_element = save_element_album(file, captions, caption_dir, dates)
                await bot.download_file(save_element[0], save_element[1])

        else:
            pass
    else:
        pass
