from basics import * #Importar modulo para manejar algunas respuestas
from config import * #Importar el Token
from visuales import new_visual #Importar modulo para trabajar los visuales
import telebot #Para la Api de Telegram

#Instanciar el Bot
bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=['start'])# Manejar mensajes /start
def handle_start(message):
    try:
        start_command(bot, message)
        user_id = message.from_user.id
    except Exception as e:# En caso de error
        print(f"Error al manejar el comando /start: {e}")

@bot.message_handler(commands=['help'])# Manejar mensajes /help
def handle_help(message):
    try:
        help_command(bot, message)
        user_id = message.from_user.id
    except Exception as e:# En caso de error
        print(f"Error al manejar el comando /help: {e}")

@bot.message_handler(commands=['newvisual'])# Manejar mensajes /newvisual
def handle_newvisual(message):
    try:
        new_visual(bot, message)
        user_id = message.from_user.id
    except Exception as e:# En caso de error
        print(f"Error al manejar el comando /newvisual: {e}")

@bot.message_handler(func=lambda message: True)#Responde a los mensajes de texto y comandos desconocidos
def handle_message(message):
    try:# Logica a ejecutar
        unknw_command(bot, message)
        user_id = message.from_user.id
        pass
    except Exception as e:# En caso de error
        print(f"Error al manejar el mensaje desconocido: {e}")

#Iniciar bot y mostrar estado en consola
print('Bot a la escucha...')
bot.infinity_polling()
print('Bot apagado...')