#Responder a /start
def help_command(bot, message):
    bot.reply_to(message, "Hola, Bienvenidos a mi Bot",parse_mode='Markdown')

#Responder a /help
def help_command(bot, message):
    bot.reply_to(message, "Actualmente no hay comandos disponibles.",parse_mode='Markdown')