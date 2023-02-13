from telegram import Update
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters

import logging

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

import ephem

logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {'proxy_url': config['PROXY']['proxy_url'],
    'urllib3_proxy_kwargs': {'username': config['PROXY']['username'], 'password': config['PROXY']['password']}}

async def greet_user(update, context):
    await update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

async def echo(update, context):
    await update.message.reply_text(update.message.text)

async def planet(update, context):
    planet = update.message.text.split()[1]
    if planet == 'Mars':
        result = ephem.Mars('2023/02/13')
    
    elif planet == 'Mercury':
        result = ephem.Mercury('2023/02/13')
        
    elif planet == 'Venus':
        result = ephem.Venus('2023/02/13')
        
    elif planet == 'Jupiter':
        result = ephem.Jupiter('2023/02/13')
        
    elif planet == 'Saturn':
        result = ephem.Saturn('2023/02/13')
        
    elif planet == 'Uranus':
        result = ephem.Uranus('2023/02/13')
        
    elif planet == 'Neptune':
        result = ephem.Neptune('2023/02/13')

    else:
        await update.message.reply_text('No such planet exists. Try again!')
    constellation = ephem.constellation(result)

    await update.message.reply_text(', '.join(constellation))

def main():
    #print(config['LOGIN']['token'])

    mybot = ApplicationBuilder().token('6282992484:AAEUdk1Yr420aEuMM4rsV6gG5YDtUlge1OY').build()
    logging.info('Бот стартовал')

    mybot.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    mybot.add_handler(CommandHandler("planet", planet))

    mybot.add_handler(CommandHandler('start', greet_user))
    mybot.run_polling()


if __name__ == "__main__":
    main()
    print(ephem.constellation)