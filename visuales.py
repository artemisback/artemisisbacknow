from db_works import load_visuales_db, save_visuales_db # IMPORTAMOS LAS FUNCIONES NECESARIAS

def new_visual(bot, message):#Preguntar por el nombre
    user_id = message.from_user.id
    bot.send_message(user_id, "💠 Para establecer un nuevo visual necesito varios datos, empecemos por el nombre, envíamelo a continuacion:\n\nRecuerda que puede cancelar la operación en cualquier momento enviando la cadena: (cancelar)", parse_mode='Markdown')
    bot.register_next_step_handler(message, obtener_nombre_del_visual, bot)

def obtener_nombre_del_visual(message, bot):#Verificar el nombre y pedir tipo
    user_id = message.from_user.id
    longitud_del_nombre = len(message.text)
    if message.text == "cancelar":
        bot.send_message(user_id, "❌ Operación cancelada!", parse_mode='Markdown')
    elif longitud_del_nombre <= 60:
        nombre_del_visual = message.text
        bot.send_message(user_id, "💠 Ahora envíame el tipo de elemento.\n\nEjemplo:\n`filme`\n`serie`\n`novela`\n`documental`\n`animado`\n\nPuedes cancelar en cualquier momento.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_tipo_del_visual, nombre_del_visual, bot)
    else:
        bot.send_message(user_id, "❌ Enviaste un nombre muy largo!\n\nEl límite de caracteres para el nombre es de 60.\n\nVuelve a intentarlo.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_nombre_del_visual, bot)

def obtener_tipo_del_visual(message, nombre_del_visual, bot):#Verificar tipo y pedir los detalles
    user_id = message.from_user.id
    longitud_del_tipo = len(message.text)
    if message.text == 'cancelar':
        bot.send_message(user_id, "❌ Operación cancelada!", parse_mode='Markdown')
    elif longitud_del_tipo <= 20 and message.text == 'filme' or message.text == 'serie' or message.text == 'novela' or message.text == 'documental' or message.text == 'animado':
        tipo_del_visual = message.text
        bot.send_message(user_id, "💠 Ahora envíame la información\n\nPuedes cancelar en cualquier momento.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_detalles_del_visual, tipo_del_visual, nombre_del_visual, bot)
    else:
        bot.send_message(user_id, "❌ Enviaste un mensaje muy largo o incorrecto!\n\nEl límite de caracteres para el nombre es de 20.\n\nVuelve a intentarlo.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_tipo_del_visual, nombre_del_visual, bot)

def obtener_detalles_del_visual(message, tipo_del_visual, nombre_del_visual, bot):#Verifiicar los detalles y pedir la fecha de estreno
    user_id = message.from_user.id
    longitud_del_detalle = len(message.text)
    if message.text == 'cancelar':
        bot.send_message(user_id, "❌ Operación cancelada!", parse_mode='Markdown')
    elif longitud_del_detalle <= 400:
        detalles_del_visual = message.text
        bot.send_message(user_id, "💠 Ahora envíame la fecha de estreno\n\nPuedes cancelar en cualquier momento.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_estreno_del_visual, detalles_del_visual, tipo_del_visual, nombre_del_visual, bot)
    else:
        bot.send_message(user_id, "❌ Enviaste un mensaje muy largo!\n\nEl límite de caracteres para el nombre es de 400.\n\nVuelve a intentarlo.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_detalles_del_visual, tipo_del_visual, nombre_del_visual, bot)

def obtener_estreno_del_visual(message, detalles_del_visual, tipo_del_visual, nombre_del_visual, bot):#Verifiicar estreno y pedir genero
    user_id = message.from_user.id
    longitud_del_estreno = len(message.text)
    if message.text == 'cancelar':
        bot.send_message(user_id, "❌ Operación cancelada!", parse_mode='Markdown')
    elif longitud_del_estreno <= 30:
        estreno_del_visual = message.text
        bot.send_message(user_id, "💠 Ahora envíame el género\n\n`Acción`, `Aventura`, `Catástrofe`, `Ciencia_Ficción`, `Comedia`, `Documentales`, `Drama`, `Fantasía`, `Musicales`, `Suspenso`, `Terror`\n\nPuedes cancelar en cualquier momento.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_genero_del_visual, estreno_del_visual, detalles_del_visual, tipo_del_visual, nombre_del_visual, bot)
    else:
        bot.send_message(user_id, "❌ Enviaste un mensaje muy largo!\n\nEl límite de caracteres para el nombre es de 30.\n\nVuelve a intentarlo.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_estreno_del_visual, detalles_del_visual, tipo_del_visual, nombre_del_visual, bot)

def obtener_genero_del_visual(message, estreno_del_visual, detalles_del_visual, tipo_del_visual, nombre_del_visual, bot):#Verifiicar el genero y guardar datos
    user_id = message.from_user.id
    longitud_del_genero = len(message.text)
    if message.text == 'cancelar':
        bot.send_message(user_id, "❌ Operación cancelada!", parse_mode='Markdown')
    elif longitud_del_genero <= 50 and message.text == 'Acción' or message.text == 'Aventura' or message.text == 'Catástrofe' or message.text == 'Ciencia_Ficción' or message.text == 'Comedia' or message.text == 'Documentales' or message.text == 'Drama' or message.text == 'Fantasía' or message.text == 'Musicales' or message.text == 'Suspenso' or message.text == 'Terror':
        genero_del_visual = message.text
        bot.send_message(user_id, "💠 Estoy guardando los datos espera un momento...", parse_mode='Markdown')
        # AQUI VA LA MECANICA PARA GUARDAR LOS DATOS NUEVOS EN LA DB (YO ME ENCARGO DE ESTO)
        bot.send_message(user_id, f"💠 LISTO:\n\nLos datos son:\n{nombre_del_visual}\n{tipo_del_visual}\n{detalles_del_visual}\n{estreno_del_visual}\n{genero_del_visual}", parse_mode='Markdown')
        print("SALVADO CON EXITO")
    else:
        bot.send_message(user_id, "❌ Enviaste un mensaje muy largo o incorrecto!\n\nEl límite de caracteres para el nombre es de 50.\n\nVuelve a intentarlo.", parse_mode='Markdown')
        bot.register_next_step_handler(message, obtener_genero_del_visual, estreno_del_visual, detalles_del_visual, tipo_del_visual, nombre_del_visual, bot)