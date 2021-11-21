import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси. Используем ради интереса
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    # print(update)
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main():
    # Создаем бота и передаем ему токен, выданный BOTfather при регистрации нашего бота
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher # запускаем диспитчер
    dp.add_handler(CommandHandler('start', greet_user)) # запускаем обработчик
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    # Включаем логирование
    logging.info("Бот стартовал")

    # Комманда для запуска обращения бота к телеграмму с запросом о наличие новых сообщений
    mybot.start_polling()

    # Запуск бота. Будет работать до принудительного останова.
    mybot.idle()

if __name__ == "__main__":
    main()