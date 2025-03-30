import telebot
import random

bot = telebot.TeleBot('7707953731:AAHWxvv8A_m-AqYlc5m6RLGNSbQ7b-w9_OU')

# Список эко-советов
eco_tips = [
    "Используйте многоразовые сумки вместо пластиковых.",
    "Экономьте воду: выключайте кран, когда чистите зубы!",
    "Сортируйте мусор",
    "Сократите потребление одноразового пластика.",
    "Используйте общественный транспорт или электро-машины вместо машин на газе/бензине."
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я эко-бот. Напиши /eco_tip, чтобы получить совет по экологии!")

@bot.message_handler(commands=['eco_tip'])
def eco_tip(message):
    tip = random.choice(eco_tips)
    bot.send_message(message.chat.id, tip)

bot.polling()
