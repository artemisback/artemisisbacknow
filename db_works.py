import json # Importar JSON para trabajar los archivos asociados

vdb = 'visuales_db.json'# DEFINIR BASES DE DATOS DE LOS VISUALES
jdb = 'juegos_db.json'# DEFINIR BASES DE DATOS DE LOS JUEGOS

def load_visuales_db():# CARGAR LA BASE DE DATOS DE VISUALES
    try:
        with open(vdb, 'r') as file:
            lista_de_visuales = json.load(file)
            return lista_de_visuales.get('visuales', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def load_juegos_db():# CARGAR LA BASE DE DATOS DE JUEGOS
    try:
        with open(jdb, 'r') as file:
            lista_de_juegos = json.load(file)
            return lista_de_juegos.get('juegos', [])
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_visuales_db(nuevo_visual):# SALVAR NUEVO VISUAL EN LA BASE DE DATOS
    visuales = load_visuales_db()
    visuales.append(nuevo_visual)
    with open(vdb, 'w') as file:
        json.dump({"visuales": visuales}, file)

def save_juegos_db(nuevo_juego):# SALVAR NUEVO JUEGO EN LA BASE DE DATOS
    juegos = load_juegos_db()
    juegos.append(nuevo_juego)
    with open(jdb, 'w') as file:
        json.dump({"juegos": juegos}, file)