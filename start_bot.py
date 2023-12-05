from basics import * #Importar modulo basics
from config import * #Importar el Token
import telebot #Para la Api de Telegram
import time

#Instanciar el Bot
bot = telebot.TeleBot(telegram_token)

#Responde a las que no son comandos
@bot.message_handler(content_types="text")  
def bot_messages_texto(message):
     #Para Gestionar los Mensajes de textos recibidos
    if bot_messages_texto.text.startswith("/"):      
        bot.send_message(bot_messages_texto.chat.id, "Comando no Disponible")
    else:    
        x = bot.send_message(bot_messages_texto.chat.id, "</b><HOLA></b>", parse_mode="html",disable_web_page_preview=True )
    time.sleep(3)
    bot.edit_message_text("<u><HOLA></u>", bot_messages_texto.chat.id, x.message_id, parse_mode="html" )

# Manejar mensajes /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    start_command(bot, message)
    user_id = message.from_user.id

# Manejar mensajes /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    help_command(bot, message)
    user_id = message.from_user.id

#Escribir el Programa Principal.
    if __name__ == '__main__':
        print('Iniciando el Bot')
        bot.infinity_polling()
        print('Fin')