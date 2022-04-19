from telebot import TeleBot
from configs import TOKEN
from main import *
import sqlite3

# with open('weather.json', mode='r', encoding='UTF-8') as text_of_message:

bot = TeleBot(TOKEN)


@bot.message_handler(commands=('start', 'about', 'history'))
def command_start(message):
    chat_id = message.chat.id
    user_name = message.chat.first_name
    if message.text == '/start':
        bot.send_message(chat_id, f"Assalomu aleykum {user_name} 🤗, ob havo ma'lumotlarini tarqatuvchi bot man")
        msg = bot.send_message(chat_id, 'Shaharni kiriting... (iltimos lotin alifbosida kiriting)')
        bot.register_next_step_handler(msg, city_call)
        # city_call(message)
    elif message.text == '/about':
        bot.send_message(chat_id, f'''Bot test ravishda ishlatilmoqda... shuninig uchun kechiripquyasiz😅😅😅''')
    elif message.text == '/history':
        # bot.send_message
        pass
    # print(message)


def city_call(message):
    chat_id = message.chat.id
    src = message.text
    bot.send_message(chat_id, f'siz {src} shaxrini tanladindiz...')
    bot.send_message(chat_id, weather_forecat(src))
    bot.send_message(chat_id, f'qaytatdan kurmoqchi bulsangiz "/start" bosing')
#     bot.register_next_step_handler(msg, weather, src)
#
# def weather(message, src):
#     chat_id = message.chat.id
#     bot.send_message(chat_id, f'{weather_forecat(src)}.')


# bot.register_next_step_handler(msg, weather_forecat(city))





bot.polling(none_stop=True, interval=0)
