
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message



#def keyboard_txt2():
 #   keyboard_bilder2 = ReplyKeyboardBuilder()
  #  keyboard_bilder2.button(text='Координаты', request_location=True)

   # keyboard_bilder2.adjust(1)
    # return keyboard_bilder2.as_markup(one_time_keyboard=True)


#def keyboard_txt1():
 #   keyboard_bilder1 = ReplyKeyboardBuilder()
  #  keyboard_bilder1.button(text='📡 Смена Ямал')
   # keyboard_bilder1.button(text='⚒ Дежурный')
    # keyboard_bilder1.adjust(2)
    # return keyboard_bilder1.as_markup(one_time_keyboard=True)


reply_duty = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📡 Смена Ярославль'),
     KeyboardButton(text='⚒ Дежурный Ямал')]
], resize_keyboard=True, one_time_keyboard=True)

# def keyboard_location():
# keyboard_bilder2=ReplyKeyboardBuilder
# keyboard_bilder2.button(text='Отправить локацию', request_location=True)
# keyboard_bilder2.adjust()
# return keyboard_bilder2.as_markup()


# KeyboardButton(text='<<👋>>'),
# KeyboardButton(text='<<👍>>')
