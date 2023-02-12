from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters

import logging

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

async def greet_user(update, context):
    await update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

async def echo(update, context):
    await update.message.reply_text(update.message.text)

def main():
    mybot = ApplicationBuilder().token('6282992484:AAEUdk1Yr420aEuMM4rsV6gG5YDtUlge1OY').build()
    logging.info('Бот стартовал')

    mybot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    mybot.add_handler(CommandHandler('start', greet_user))
    mybot.run_polling()


if __name__ == "__main__":
    main()