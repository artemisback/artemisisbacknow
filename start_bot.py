from basics import * #Importar modulo basics para manejar las respuestas a los comandos de 
from config import * #Importar el Token
import telebot #Para la Api de Telegram

#Instanciar el Bot
bot = telebot.TeleBot(telegram_token)

# Manejar mensajes /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    try:
        start_command(bot, message)
        user_id = message.from_user.id
    except Exception as e:# En caso de error
        print(f"Error al manejar el comando /start: {e}")

# Manejar mensajes /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    try:
        help_command(bot, message)
        user_id = message.from_user.id
    except Exception as e:# En caso de error
        print(f"Error al manejar el comando /help: {e}")

#Responde a los mensajes de texto y comandos desconocidos
@bot.message_handler(func=lambda message: True)
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