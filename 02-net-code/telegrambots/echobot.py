import config
import telebot

# Объявляет новый объект класса TeleBot. Конструктор принимает обязательный аргумент - токен
bot = telebot.TeleBot(config.token)

# Выполнит низжестоящую функцию, если полученный запрос является текстом
@bot.massage_handler(content_type=["text"])
def echo_massages(massage):
    # Отправляет полученное сообщение обратно клиенту Telegram
    bot.send_message(massage.chat.id, massage.text)

if __name__ == "__main__":
    # Запускаем цикл Long Polling, который обрабатывает запросы со стороны Telegram
    bot.infinity_polling()