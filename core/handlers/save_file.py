
from aiogram import Bot
from aiogram.types import Message
from core.handlers.albums_save import caption_element_album, save_element_album
from core.settings import settings



async def photo_file(message: Message, bot: Bot):

    if message.from_user.id in settings.bots.duty_kamenny + settings.bots.duty_seed:
        media_group = str(message.media_group_id)
        if media_group == 'None':
            dates = str(message.date).split(' ')
            caption = str(message.caption)
            user_file = str(message.from_user.full_name)
            user_id = str(message.from_user.id)

            caption_element = caption_element_album(caption, user_file, user_id)  # проверяем подпись по фото
            captions = caption_element[0]
            caption_dir = caption_element[1]
            if caption_element[2] != 'Ignor':
                if caption_element[2] != 'None':
                    await message.answer(text=caption_element[2])

                if message.photo:
                    file = await bot.get_file(message.photo[-1].file_id)

                    # input_media = InputMediaPhoto(media=element.photo[-1].file_id, **caption_kwargs)
                elif message.video:
                    file = await bot.get_file(message.video.file_id)


                save_element = save_element_album(file, captions, caption_dir, dates)
                await bot.download_file(save_element[0], save_element[1])
            else:
                pass
        else:
            pass
    else:
        pass



