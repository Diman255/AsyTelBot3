from aiogram.utils.keyboard import InlineKeyboardBuilder

def inlain_keyboart_bot_point():
    keyboard_bilder6 = InlineKeyboardBuilder()
    keyboard_bilder6.button(text='<<🛻>> Выезжаем', callback_data='exit_local')
    keyboard_bilder6.button(text='<<🏚>>Прибыл', switch_inline_query_current_chat = 'location_duty')
# ', url='https://t.me/JymiLov_bot'
    keyboard_bilder6.button(text='<<🚁>> Завершение дежурства', callback_data='exit_duty_local')
    keyboard_bilder6.adjust(2)
    return keyboard_bilder6.as_markup()

def inlain_keyboart_chat():
    keyboard_bilder7 = InlineKeyboardBuilder()
    keyboard_bilder7.button(text='Закрыть', url='t.me/+EicGwaUgT9sxODMy')

    keyboard_bilder7.adjust(1)
    return keyboard_bilder7.as_markup()

def inlain_keyboart_start_yaroclavl ():
    keyboard_bilder8 = InlineKeyboardBuilder()
    keyboard_bilder8.button(text='<<👋>> Дежурный', callback_data='duty_yaroclavl')
    keyboard_bilder8.button(text='<<👍>> Принял', callback_data='accepted_yaroclavl')

    keyboard_bilder8.adjust(2)
    return keyboard_bilder8.as_markup()


def inlain_keyboart_kamenny():
    keyboard_bilder = InlineKeyboardBuilder()
    keyboard_bilder.button(text='Т1 Ямбург', callback_data='tower_T1 Ямбург' )
    keyboard_bilder.button(text='T2 Сайт 1', callback_data='tower_T2 Сайт 1')
    keyboard_bilder.button(text='T3 Парусный ', callback_data='tower_T3 Парусный')
    keyboard_bilder.button(text='T4 Каменный', callback_data='tower_T4 М.Каменный')
    keyboard_bilder.button(text='T5 Сайт 11', callback_data='tower_T5 Сайт 11')
    keyboard_bilder.button(text='T6 Пилар', callback_data='tower_T6 Пилар')
    keyboard_bilder.button(text='T7 Сайт 16', callback_data='tower_T7 Сайт 16')
    keyboard_bilder.button(text='T8 Сайт 9', callback_data='tower_T8 Сайт 9')
    keyboard_bilder.button(text='Каменный', callback_data='tower_п. Мыс Каменный')


    keyboard_bilder.adjust(3)
    return keyboard_bilder.as_markup()




def inlain_keyboart_seed():
    keyboard_bilder1 = InlineKeyboardBuilder()
    keyboard_bilder1.button(text='Т9  Яптик-Сале', callback_data='tower_T9  Яптик-Сале' )
    keyboard_bilder1.button(text='T10 Сайт 2', callback_data='tower_T10 Сайт 2')
    keyboard_bilder1.button(text='T11 Cайт 3 ', callback_data='tower_T11 Cайт 3')
    keyboard_bilder1.button(text='T12 Cеяха', callback_data='tower_T12 Cеяха')
    keyboard_bilder1.button(text='T13 Сайт 13', callback_data='tower_T13 Сайт 13')
    keyboard_bilder1.button(text='T14 Cайт 8', callback_data='tower_T14 Cайт 8')
    keyboard_bilder1.button(text='T15 ТА', callback_data='tower_T15 ТА')
    keyboard_bilder1.button(text='T16 Сабетта', callback_data='tower_T16 Сабетта')
    keyboard_bilder1.button(text='Сеяха', callback_data='tower_п. Сеяха')

    keyboard_bilder1.adjust(3)
    return keyboard_bilder1.as_markup()



def inlain_keyboart_kamenny_arrived():
    keyboard_bilder2 = InlineKeyboardBuilder()
    keyboard_bilder2.button(text='Т1 Ямбург', callback_data='arrived_T1 Ямбург' )
    keyboard_bilder2.button(text='T2 Сайт 1', callback_data='arrived_T2 Сайт 1')
    keyboard_bilder2.button(text='T3 Парусный ', callback_data='arrived_T3 Парусный')
    keyboard_bilder2.button(text='T4 Каменный', callback_data='arrived_T4 М.Каменный')
    keyboard_bilder2.button(text='T5 Сайт 11', callback_data='arrived_T5 Сайт 11')
    keyboard_bilder2.button(text='T6 Пилар', callback_data='arrived_T6 Пилар')
    keyboard_bilder2.button(text='T7 Сайт 16', callback_data='arrived_T7 Сайт 16')
    keyboard_bilder2.button(text='T8 Сайт 9', callback_data='arrived_T8 Сайт 9')
    keyboard_bilder2.button(text='Каменный', callback_data='arrived_п. Мыс Каменный')


    keyboard_bilder2.adjust(3)
    return keyboard_bilder2.as_markup()



def inlain_keyboart_seed_arrived():
    keyboard_bilder3 = InlineKeyboardBuilder()
    keyboard_bilder3.button(text='Т9  Яптик-Сале', callback_data='arrived_T9  Яптик-Сале' )
    keyboard_bilder3.button(text='T10 Сайт 2', callback_data='arrived_T10 Сайт 2')
    keyboard_bilder3.button(text='T11 Cайт 3 ', callback_data='arrived_T11 Cайт 3')
    keyboard_bilder3.button(text='T12 Cеяха', callback_data='arrived_T12 Cеяха')
    keyboard_bilder3.button(text='T13 Сайт 13', callback_data='arrived_T13 Сайт 13')
    keyboard_bilder3.button(text='T14 Cайт 8', callback_data='arrived_T14 Cайт 8')
    keyboard_bilder3.button(text='T15 ТА', callback_data='arrived_T15 ТА')
    keyboard_bilder3.button(text='T16 Сабетта', callback_data='arrived_T16 Сабетта')
    keyboard_bilder3.button(text='Сеяха', callback_data='arrived_п. Сеяха')

    keyboard_bilder3.adjust(3)
    return keyboard_bilder3.as_markup()