import telebot
import datetime

# 🔐 Твой токен:
TOKEN = "7715426459:AAHhPvFrZrqDXE0Jlqhv0g98ra41xPRv_G0"

bot = telebot.TeleBot(TOKEN)

# Приветственное сообщение
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, королева мотивации! 👑 Готова достигать цели? 💰")

# Обработка отчётов
@bot.message_handler(func=lambda msg: True)
def handle_message(message):
    text = message.text.lower()
    now = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')

    if "отчёт" in text or "сделала" in text or "сделал" in text:
        bot.send_message(message.chat.id, f"💪 Молодец! Принято в {now}. Так держать!")
    elif "не успела" in text or "не сделал" in text:
        bot.send_message(message.chat.id, "😢 Ничего страшного! Завтра точно получится. Главное — не сдаваться!")
    else:
        bot.send_message(message.chat.id, "Напомни, ты хочешь отправить отчёт? Напиши, что сделала или не успела 💌")

bot.polling()
