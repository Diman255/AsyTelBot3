
import asyncio
from aiogram import Bot
from core.utils.symm_archive import summ_archive
from aiogram.types import FSInputFile
from core.settings import settings

async def timing_archive(bot: Bot):
    print('запуск по таймеру')
    result = summ_archive()
    text1 = result[0]



    if text1 == 'Архив фото и видео':
        path_sum = result[2]
        await bot.send_message(chat_id=settings.bots.chat_grup, text=text1)
        for patch in path_sum:
            print(patch)
            asd = FSInputFile(patch)
            await bot.send_document(chat_id=settings.bots.chat_grup, document=asd, disable_content_type_detection=False)
            await asyncio.sleep(10)

        text2 = result[1]
        if text2 != 'None':
            await bot.send_message(chat_id=settings.bots.chat_grup, text=text1)

    else:
        await bot.send_message(chat_id=settings.bots.chat_grup, text=text1)
    # symm_archives_delete()