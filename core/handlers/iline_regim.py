import hashlib
from core.utils.local_file_obyekt import local_file_obyect_save
from aiogram.types import InlineQuery, InlineQueryResult, InlineQueryResultArticle, InputTextMessageContent
from aiogram import Bot
from core.utils.jymal_obyect import local_tower


async def location_exit(inline: InlineQuery, bot: Bot):
    location = str(inline.location)
    if location != 'None':
        longitude = int(float(inline.location.longitude) * 1000000)
        latitude = int(float(inline.location.latitude) * 1000000)

        print(longitude, latitude)
        print(inline)
        local_stat_pazn = {}
        vne_radiusa = 0

        local_stat = local_tower()

        for key, value in local_stat.items():

            sh_razn = longitude - value[0]
            dg_razn = latitude - value[1]
            vektor_ract = sh_razn * sh_razn + dg_razn * dg_razn
            if vektor_ract < 4396159600:
                local_stat_pazn[key] = (vektor_ract)
                vne_radiusa = 10

        if vne_radiusa == 10:
            obyekt = min(local_stat_pazn, key=local_stat_pazn.get)
            print(local_stat_pazn, obyekt)
            # добавляем объект и дежурного для имени файла для записи
            id_users = str(inline.from_user.id)
            local_file_obyect_save(id_users, obyekt)
            text = f'<u><b>{inline.from_user.full_name} - </b></u> Прибыл на {obyekt} координаты {longitude}:{latitude}'
            in_text = InputTextMessageContent(message_text=text)
            id_result = str(hashlib.md5(str(inline.id).encode()).hexdigest())
            title_text = f'⭕️ {obyekt} Подтверждаю'
            results_local = InlineQueryResultArticle(input_message_content=in_text,
                                                     id=id_result, title=title_text)

        else:
            # добавляем объект и дежурного для имени файла для записи

            text = f'<u><b>{inline.from_user.full_name},</b></u> не удалось определить объект.\n Ваши координаты: \n' \
                   f' Широта: {longitude}, \n Долгота: {latitude}.'
            in_text = InputTextMessageContent(message_text=text)
            id_result = str(hashlib.md5(str(inline.id).encode()).hexdigest())
            title_text = f'‼️ Некорректные данные  ❌'
            results_local = InlineQueryResultArticle(input_message_content=in_text,
                                                     id=id_result, title=title_text)
    else:
        text = f'<u><b>{inline.from_user.full_name},</b></u> у вас выключена геолокация. ' \
               f'Включите определение геолокации ' \
               f' и повторите выждав через минуту.'
        in_text = InputTextMessageContent(message_text=text)
        id_result = str(hashlib.md5(str(inline.id).encode()).hexdigest())
        title_text = f'‼️ Выключена Геолокация  ❌'
        results_local = InlineQueryResultArticle(input_message_content=in_text,
                                                 id=id_result, title=title_text)

    await bot.answer_inline_query(inline_query_id=inline.id, results=[results_local], cache_time=3, is_personal=True)
