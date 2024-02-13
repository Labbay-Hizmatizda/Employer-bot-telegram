import sqlite3
import telebot

bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')

user_data = {}

# conn = sqlite3.connect('users.sqlite3', check_same_thread=False)
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS workers (
#                     id INTEGER PRIMARY KEY AUTOINCREMENT,
#                     user_id INTEGER,
#                     user_name TEXT,
#                     birthday TEXT,
#                     passport TEXT,
#                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                 )''')

# cursor.execute('''CREATE TABLE workers (
#                     id INTEGER PRIMARY KEY,
#                     user_id INTEGER,
#                     user_name TEXT,
#                     birthday TEXT,
#                     passport_number_and_series TEXT,
#                     born_date TEXT,
#                     born_place TEXT,
#                     sex TEXT,
#                     given_date TEXT
# );''')


@bot.message_handler(commands=['start'])
def handle_worker_info(message):
    user_id = message.from_user.id
    user_name = message.text

    # Save user information to the database
    # cursor.execute("INSERT INTO workers (user_id, user_name) VALUES (?, ?)", (user_id, user_name))
    # conn.commit()

    bot.send_message(user_id, "Теперь введите ваше имя, фамилия, отчество.. ")
    bot.register_next_step_handler(message, handle_worker_birthday)


def handle_worker_birthday(message):
    user_id = message.from_user.id
    user_birthday = message.text

    # Save user birthday to the database
    # cursor.execute("UPDATE workers SET birthday=? WHERE user_id=?", (user_birthday, user_id))
    # conn.commit()

    bot.send_message(user_id, "Теперь введите ваши паспортные данные (серия и номер).. ")
    bot.register_next_step_handler(message, handle_worker_passport)


def handle_worker_passport(message):
    user_id = message.from_user.id
    user_passport = message.text

    bot.send_message(user_id, "Теперь введите дату выдачи паспорта (дд.мм.гггг).. ")
    bot.register_next_step_handler(message, lambda msg: handle_worker_passport_given_date(msg, user_passport))


def handle_worker_passport_given_date(message, user_passport):
    user_id = message.from_user.id
    given_date = message.text

    bot.send_message(user_id, "Теперь введите дату рождения (дд.мм.гггг).. ")
    bot.register_next_step_handler(message,
                                   lambda msg: handle_worker_passport_born_date(msg, user_passport, given_date))


def handle_worker_passport_born_date(message, user_passport, given_date):
    user_id = message.from_user.id
    born_date = message.text

    bot.send_message(user_id, "Теперь введите место рождения.. ")
    bot.register_next_step_handler(message,
                                   lambda msg: handle_worker_passport_born_place(msg, user_passport, given_date,
                                                                                 born_date))


def handle_worker_passport_born_place(message, user_passport, given_date, born_date):
    user_id = message.from_user.id
    born_place = message.text

    bot.send_message(user_id, "Теперь введите пол (мужской/женский).. ")
    bot.register_next_step_handler(message,
                                   lambda msg: handle_worker_passport_sex(msg, user_passport, given_date, born_date,
                                                                          born_place))


def handle_worker_passport_sex(message, user_passport, given_date, born_date, born_place):
    user_id = message.from_user.id
    sex = message.text

    # Save user passport information to the database
    # cursor.execute(
    #     "UPDATE workers SET passport_number_and_series=?, given_date=?, born_date=?, born_place=?, sex=? WHERE user_id=?",
    #     (user_passport, given_date, born_date, born_place, sex, user_id))
    # conn.commit()

    bot.send_message(user_id, "Паспортные данные успешно сохранены!")

    bot.send_message(user_id,
                     "Отлично! Теперь вы можете использовать команду /services для просмотра доступных действий.")


@bot.message_handler(commands=['services'])
def add_service(message):
    bot.send_message(message.chat.id, "Please provide the service name:")
    bot.register_next_step_handler(message, get_service_name)


def get_service_name(message):
    service_name = message.text
    user_id = message.from_user.id
    user_data[user_id] = {"service_name": service_name}
    bot.send_message(user_id, "Please provide the service description:")
    bot.register_next_step_handler(message, get_service_description)


def get_service_description(message):
    service_description = message.text
    user_id = message.from_user.id
    user_data[user_id]["service_description"] = service_description
    bot.send_message(user_id, "Please provide the service price:")
    bot.register_next_step_handler(message, get_service_price)


def get_service_price(message):
    service_price = message.text
    user_id = message.from_user.id
    user_data[user_id]["service_price"] = service_price
    bot.send_message(user_id, "Please provide the service location:")
    bot.register_next_step_handler(message, get_service_location)


def get_service_location(message):
    service_location = message.text
    user_id = message.from_user.id
    user_data[user_id]["service_location"] = service_location

    # cursor.execute(
    #     "INSERT INTO services (user_id, service_name, service_description, service_price, service_location) VALUES (?, ?, ?, ?, ?)",
    #     (user_id, user_data[user_id]["service_name"], user_data[user_id]["service_description"],
    #      user_data[user_id]["service_price"], user_data[user_id]["service_location"]))
    # conn.commit()

    bot.send_message(user_id, "Service added successfully!")


def new_request(pk, message):
    # TODO: identify the user by pk and get the message to request from him | add buttons with accept request,
    #  ignore request, deny request, send him a message about, does his request denied or accepted, do not inform him
    #  if it was ignored
    pass


@bot.message_handler(commands=['requests'])
def list_of_requests(message):
    # TODO: list of requests for the user | add buttons with accept request, ignore request, deny request,
    #  send him a message about,
    #  does his request denied or accepted, do not inform him if it was ignored
    pass


@bot.message_handler(commands=['services'])
def list_of_services(message):
    # TODO: list of his services for the user | add buttons with edit service, delete service
    pass


if __name__ == "__main__":
    bot.polling(none_stop=True)
