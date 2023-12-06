#Responder a /start
def start_command(bot, message):
    bot.reply_to(message, "Hola, Bienvenidos a mi Bot",parse_mode='Markdown')

#Responder a /help
def help_command(bot, message):
    bot.reply_to(message, "Actualmente no hay comandos disponibles.",parse_mode='Markdown')

#Responder a comandos desconocidos
def unknw_command(bot, message):
    bot.reply_to(message, "Comando incorrecto, usa /help para ver una lista de comandos actualizados.",parse_mode='Markdown')