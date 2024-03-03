import telebot
from markup import *

bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')
user_lang = {}

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.InlineKeyboardMarkup()
    lang_rus = types.InlineKeyboardButton('🇷🇺 Русский', callback_data='lang_rus')
    lang_uz = types.InlineKeyboardButton('🇺🇿 O\'zbek tili', callback_data='lang_uz')

    markup.add(lang_rus, lang_uz)
    bot.send_message(message.chat.id, "Выберите язык 🌐\nTilni tanlang 🌐", reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call): 
    if call.data == 'lang_rus':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='Привет, {0}!'.format(call.from_user.first_name), reply_markup=markup)
    elif call.data == 'about_us_rus':
        markup = types.InlineKeyboardMarkup()
        back = types.InlineKeyboardButton('Назад', callback_data='back')
        markup.add(back)

        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="У наc сайт хотите посетить", reply_markup=markup)

        '''
            -Мои данные
                -Изменить номер
                -Изменить пароль от аккаунта 
                -Назад
        '''
    elif call.data == 'my_account_rus':
        markup = my_account_rus()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций :", reply_markup=markup)
    elif call.data == 'change_number':
        ...
    elif call.data == 'back':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций:", reply_markup=markup)



        '''
            -Заказы
                -активные заказы
                -новые заказы
                -назад
        '''
    elif call.data == 'orders_rus':
        markup = orders_rus()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций :", reply_markup=markup)
    elif call.data == 'active_orders':
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Какую одну из функций :")
    elif call.data == 'new_order':
        pass
    elif call.data == 'back':
        markup = russian()
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.id, text="Вы в главном меню \nКакое действие вы хотите сделать :z", reply_markup=markup)


@bot.message_handler(commands=['login'])
def log_into(message):
    ...


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю эту команду. Попробуйте /help для списка команд.")


if __name__ == "__main__":
    print('\n.', '.', '.\n')
    bot.polling(none_stop=True)


















'''Вывод деталей ------------------------------------------------------------------------------------------------------------'''
# @bot.message_handler(func=lambda message: message.text == "Мои данные")
# def handle_my_actions(message):
#     # Получаем информацию о пользователе
#     username = message.from_user.username
#     user_id = message.from_user.id
#     phone_number = message.contact.phone_number
#     # bot.send_message(message.chat.id, f'Спасибо, @{username}! Ваш номер телефона: {phone_number}')

#     # Запрашиваем номер телефона
#     bot.send_message(message.chat.id, f'Привет, @{username}! Пожалуйста, отправьте свой номер телефона.')
    
#     # Обработчик для получения номера телефона
# @bot.message_handler(content_types=['contact'])
# def handle_contact(message):
#     phone_number = message.contact.phone_number
#     bot.send_message(message.chat.id, f'Спасибо, @! Ваш номер телефона: {phone_number}')