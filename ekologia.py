import telebot
import random

bot = telebot.TeleBot('???')

# Список эко-советов
eco_tips = [
    "Используйте многоразовые сумки вместо пластиковых.",
    "Экономьте воду: выключайте кран, когда чистите зубы!",
    "Сортируйте мусор",
    "Сократите потребление одноразового пластика.",
    "Используйте общественный транспорт или электро-машины вместо машин на газе/бензине."
]

# Вопросы для эко-викторины
quiz_questions = [
    {
        "question": "Сколько лет разлагается пластиковая бутылка?",
        "options": ["10 лет", "100 лет", "450 лет"],
        "answer": "450 лет"
    },
    {
        "question": "Что из этого подлежит переработке?",
        "options": ["Банановая кожура", "Стеклянная бутылка", "Грязная салфетка"],
        "answer": "Стеклянная бутылка"
    },
    {
        "question": "Что помогает сократить выбросы CO2?",
        "options": ["Частое использование машины", "Посадка деревьев", "Сжигание мусора"],
        "answer": "Посадка деревьев"
    }
]

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я эко-бот.\n"
        "Напиши /eco_tip, чтобы получить эко-совет.\n"
        "Напиши /eco_quiz, чтобы пройти викторину!"
    )

@bot.message_handler(commands=['eco_tip'])
def eco_tip(message):
    tip = random.choice(eco_tips)
    bot.send_message(message.chat.id, tip)

@bot.message_handler(commands=['eco_quiz'])
def eco_quiz(message):
    quiz = random.choice(quiz_questions)
    question = quiz["question"]
    options = quiz["options"]
    correct_answer = quiz["answer"]

    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for option in options:
        markup.add(option)

    msg = bot.send_message(message.chat.id, f"❓ Вопрос:\n{question}", reply_markup=markup)
    bot.register_next_step_handler(msg, check_answer, correct_answer)

def check_answer(message, correct_answer):
    user_answer = message.text
    if user_answer == correct_answer:
        bot.send_message(message.chat.id, "✅ Правильно!", reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        bot.send_message(message.chat.id, f"❌ Неправильно. Правильный ответ: {correct_answer}", reply_markup=telebot.types.ReplyKeyboardRemove())

bot.polling()
