import telebot
import time

bot = telebot.TeleBot("7715426459:AAHhPvFrZrqDXE0Jlqhv0g98ra41xPRv_G0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Я MotivationQueenBot 👑. Я буду помогать тебе двигаться к цели!")

while True:
    try:
        bot.polling()
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(15)
