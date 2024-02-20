import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot('6956163861:AAHiedP7PYOWS-QHeLSqyhGtJsm5aSkFrE8')

user_data = {}

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS workers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    user_name TEXT,
                    birthday TEXT,
                    passport_number_and_series TEXT,
                    given_date TEXT,
                    born_date TEXT,
                    born_place TEXT,
                    sex TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS services (
                    user_id INTEGER,
                    service_name TEXT,
                    service_description TEXT,
                    service_price REAL,
                    service_location TEXT
                )''')
""" sqlite passport creation code
cursor.execute('''
    CREATE TABLE IF NOT EXISTS passport (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        born_date TEXT NOT NULL,
        born_place TEXT NOT NULL,
        sex TEXT NOT NULL,
        passport_number_and_series TEXT NOT NULL,
        given_date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES workers (id)
    )
''')
"""


@bot.message_handler(commands=['start'])
def handle_worker_info(message):
    user_id = message.from_user.id
    user_name = message.text
    cursor.execute("SELECT * FROM workers WHERE user_id=?", (user_id,))
    existing_user = cursor.fetchone()
    if existing_user:
        print("User exists")
        # TODO: Hello message to user | adding markups
    else:
        user_data[user_id] = {"user_name": user_name}

        bot.send_message(user_id, "Теперь введите вашу дату рождения (дд.мм.гггг):")
        bot.register_next_step_handler(message, handle_worker_birthday)



def handle_worker_birthday(message):
    user_id = message.from_user.id
    user_birthday = message.text

    user_data[user_id]["birthday"] = user_birthday

    bot.send_message(user_id, "Теперь введите ваши паспортные данные (серия и номер):")
    bot.register_next_step_handler(message, handle_worker_passport)


def handle_worker_passport(message):
    user_id = message.from_user.id
    user_passport = message.text

    user_data[user_id]["passport"] = user_passport

    bot.send_message(user_id, "Теперь введите дату выдачи паспорта (дд.мм.гггг):")
    bot.register_next_step_handler(message, handle_worker_passport_given_date)


def handle_worker_passport_given_date(message):
    user_id = message.from_user.id
    given_date = message.text

    bot.send_message(user_id, "Теперь введите дату рождения (дд.мм.гггг):")
    bot.register_next_step_handler(message, lambda msg: handle_worker_passport_born_date(msg, given_date))


def handle_worker_passport_born_date(message, given_date):
    user_id = message.from_user.id
    born_date = message.text

    bot.send_message(user_id, "Теперь введите место рождения:")
    bot.register_next_step_handler(message, lambda msg: handle_worker_passport_born_place(msg, given_date, born_date))


def handle_worker_passport_born_place(message, given_date, born_date):
    user_id = message.from_user.id
    born_place = message.text

    bot.send_message(user_id, "Теперь введите пол (мужской/женский):")
    bot.register_next_step_handler(message, lambda msg: handle_worker_passport_sex(msg, given_date, born_date, born_place))


def handle_worker_passport_sex(message, given_date, born_date, born_place):
    user_id = message.from_user.id
    sex = message.text

    user_info = user_data[user_id]
    user_name = user_info["user_name"]
    user_birthday = user_info["birthday"]
    user_passport = user_info["passport"]

    cursor.execute("INSERT INTO workers (user_id, user_name, birthday, passport_number_and_series, given_date, born_date, born_place, sex) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (user_id, user_name, user_birthday, user_passport, given_date, born_date, born_place, sex))
    conn.commit()

    bot.send_message(user_id, "Паспортные данные успешно сохранены!")

    bot.send_message(user_id, "Отлично! Теперь вы можете использовать команду /services для просмотра доступных действий.")


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

    cursor.execute(
        "INSERT INTO services (user_id, service_name, service_description, service_price, service_location) VALUES (?, ?, ?, ?, ?)",
        (user_id, user_data[user_id]["service_name"], user_data[user_id]["service_description"],
         user_data[user_id]["service_price"], user_data[user_id]["service_location"]))
    conn.commit()
    # TODO: Send job to Channel (with button)
    bot.send_message(user_id, "Service added successfully!")


def new_request(pk, message):
    # TODO: identify the user by pk and get the message to request from him | add buttons with accept request,
    #  ignore request, deny req uest, send him a message about, does his request denied or accepted, do not inform him
    #  if it was ignored
    pass


@bot.message_handler(commands=['requests'])
def list_of_requests(message):
    # TODO: list of requests for the user | add buttons with accept request, ignore request, deny request,
    #  send him a message about,
    #  does his request denied or accepted, do not inform him if it was ignored
    pass


def get_user_services(user_id):
    conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your database file
    c = conn.cursor()
    c.execute("SELECT * FROM services WHERE user_id=?", (user_id,))
    services = c.fetchall()
    conn.close()
    return services


# Define the handler for the /services command
@bot.message_handler(commands=['services'])
def list_of_services(message):
    # Get user ID
    user_id = message.from_user.id

    # Fetch user's services from the database
    services = get_user_services(user_id)

    if not services:
        bot.reply_to(message, "You don't have any services yet.")
        return

    # Create a keyboard markup
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Iterate over each service and add it to the message with buttons
    for service in services:
        service_name = service[1]
        edit_button = types.KeyboardButton(f"Edit {service_name}")
        delete_button = types.KeyboardButton(f"Delete {service_name}")
        markup.add(edit_button, delete_button)

        # You can customize the service message as per your requirements
        service_message = f"Service Name: {service_name}\n" \
                          f"Service Description: {service[2]}\n" \
                          f"Service Price: {service[3]}\n" \
                          f"Service Location: {service[4]}\n"

        # Send the service message with buttons
        bot.send_message(message.chat.id, service_message, reply_markup=markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)