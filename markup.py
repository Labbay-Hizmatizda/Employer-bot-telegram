from telebot import types


def russian():
    markup = types.InlineKeyboardMarkup()

    about_us = types.InlineKeyboardButton('О нас', callback_data='about_us_rus')
    my_account = types.InlineKeyboardButton('Мои Данные', callback_data='my_account_rus')
    orders = types.InlineKeyboardButton('Заказы', callback_data='orders_rus')
    
    markup.add(about_us, my_account, orders)
    return markup

#-------------------------------------------------------------------------------
def my_account_rus():
    markup = types.InlineKeyboardMarkup()

    change_phone_number = types.InlineKeyboardButton('Изменить номер', callback_data='change_number')
    back = types.InlineKeyboardButton('◀ Назад', callback_data='back')
    markup.add(change_phone_number, back)
    return markup

def change_phone_num():
    ...

#-------------------------------------------------------------------------------
def orders_rus():
    markup = types.InlineKeyboardMarkup()

    active_orders = types.InlineKeyboardButton('Активные заказы', callback_data='active_orders')
    new_order = types.InlineKeyboardButton('Создать новый заказ', callback_data='new_order')
    back = types.InlineKeyboardButton('◀ Назад', callback_data='back')
    markup.add(active_orders, new_order, back)

    return markup


def active_orders_rus():
    ...
    
def new_order():
    ...

#-------------------------------------------------------------------------------
def login():
    ...

def register():
    ...

    
# def uzbek():
#     markup = types.InlineKeyboardMarkup()

#     about_us = types.InlineKeyboardButton('Biz Haqimizda', callback_data='about_us_uz')
#     my_account = types.InlineKeyboardButton('Mening danniylarim', callback_data='my_info_uz')
#     orders = types.InlineKeyboardButton('Buyurtlamarim', callback_data='orders_uz')
    
#     markup.add(about_us, my_account, orders)
#     return markup



