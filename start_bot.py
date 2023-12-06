from basics import * #Importar modulo basics
from config import * #Importar el Token
import telebot #Para la Api de Telegram
import time

#Instanciar el Bot
bot = telebot.TeleBot(telegram_token)


# Manejar mensajes /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    try:
        start_command(bot, message)
        user_id = message.from_user.id
    except Exception as e:
        print(f"Error al manejar el comando /start: {e}")

# Manejar mensajes /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    try:
        help_command(bot, message)
        user_id = message.from_user.id
    except Exception as e:
        print(f"Error al manejar el comando /help: {e}")

#Responde a los mensajes de texto
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:# Logica a ejecutar
        unknw_command(bot, message)
        user_id = message.from_user.id
        pass
    except Exception as e:# En caso de error
        print(f"Error al manejar el mensaje: {e}")

#Escribir el Programa Principal.
print('Iniciando el Bot')
bot.infinity_polling()
print('Fin')