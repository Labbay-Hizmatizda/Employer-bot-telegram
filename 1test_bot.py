import telebot
from telebot import types

bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')


@bot.message_handler(commands=['start'])
def start(message):
    # user_id = message.from_user.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang_rus = types.KeyboardButton('🇷🇺 Русский')
    lang_uz = types.KeyboardButton('🇺🇿 O\'zbek tili')

    markup.add(lang_rus, lang_uz)
    bot.send_message(message.chat.id, "Выберите язык 🌐\nTilni tanlang 🌐", reply_markup=markup)




@bot.message_handler(content_types=['text'])
def bot_message(message):
    
    if message.chat.type == 'private':
        if message.text == '🇷🇺 Русский':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            about_us = types.KeyboardButton('О нас')
            my_account = types.KeyboardButton('Мои данные')
            orders = types.KeyboardButton('Список моих заказов')
            
            markup.add(about_us, my_account, orders)
            
            bot.send_message(message.chat.id, 'Привет, {0}!..............'.format(message.from_user.first_name), reply_markup=markup)
            # smth = False
            # if message.text == 'О нас':
            #     bot.send_message(message.chat.id, 'Этот бот .....'.format(message.from_user.first_name))
            # elif message.text == 'Мои данные':
            #     bot.send_message(message.chat.id, 'Че там '.format(message.from_user.first_name))
            #     if message.from_user.username: # check if there is username of this user - True
            '''
                - зареганный username
                - пароль аккаунта
                - рейтинг аккаунта 

            '''
                   
                    
                
                # elif False:  # если username не нашел в базе тогда зарегать юзера....... 
            '''markup

                - логин (в логике должна быть /login)
                - зарегистрироваться (в логике должна быть /register)

            '''
            #         bot.send_message(message.chat.id, 'Вы еще не регались\nВыберите один из вариантов(войти, зарегистрироваться)', reply_markup=markup)

            # elif message.text == 'Список моих заказов':
            '''
            ____markup
                - мои АКТИВНЫЕ заказы (вывод список заказов в режиме active)
                    if True:
                        - список .............. 

                            !!!! список выводить в markup типа внизу вообщения(пользователя виден только именя заказов, ноооо в логике лежит id заказа) 
                            для этого в базе данных в моделе должно быть поле is_active блять Рамзиддинга эткин бомаса кошиб койсинла

                        - отследить id АКТИВНОГО заказа и ...

                            ____markupp
                                - изменить условия заказа
                                - отлики мардикоров (в логике должно быть команда например /отклик_мардыкоров)(и там выходит список всех откликов(сообщение,цена, картинка чела, номер тел) от мардкоров в виде карточки)
                                
                                
        

                - создать новый заказ (в логике лежит команда /new_order)
                - еще что-то хотел добавить но забыл
        
        '''

            '''
            responses = types.KeyboardButton('') in to my orders
            new_orders = types.KeyboardButton('')
            '''   

        # elif message.text == '🇺🇿 O\'zbek tili':
        #     bot.send_message(message.chat.id, 'Salom, {0}!...............'.format(message.from_user.first_name))





@bot.message_handler(commands=['login'])
def login(message):
    '''logging in

        - Имя, Фамилия пользователя (попросить написать имя и фамилию который был введен в тг аккаунте чтобы в дальнейшем проверять оттуда)
        - Пароль от аккаунта в боте 
        - номер телефона 
        - approve with sms code to authinticate
    
    '''

@bot.message_handler(commands=['register'])
def register(message):
    '''registration

        - все также как и в login
        - и не забыть предупредить далбаепа чтоб не забывал этот пароль 


    '''

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