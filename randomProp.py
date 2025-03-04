import random 

def escoger_usuarios_random(session):
    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    usernames = [record['username'] for record in usuarios]

    usuarios_random = random.sample(usernames, min(random.randint(1, 5), len(usernames)))
    return usuarios_random

def escoger_un_usuario_random(session):
    usuarios = session.run("MATCH (u:Usuario) RETURN u.username as username")
    usernames = [record['username'] for record in usuarios]
    usuario_random = random.choice(usernames)
    return usuario_random

def escoger_publicacion_random(session):
    
    publicaciones = session.run("MATCH (p:Publicacion) RETURN p.id_publicacion as id_publicacion")
    publicaciones = [record['id_publicacion'] for record in publicaciones]

    publicaciones_random = random.sample(publicaciones, min(2, len(publicaciones)))
    return publicaciones_random

def escoger_una_publicacion_random(session):
    
    publicaciones = session.run("MATCH (p:Publicacion) RETURN p.id_publicacion as id_publicacion")
    publicaciones = [record['id_publicacion'] for record in publicaciones]
    publicaciones_random = random.choice(publicaciones)
    return publicaciones_random


def escoger_comentarios_random(session):
    
    comentarios = session.run("MATCH (c:Comentario) RETURN c.id_comentario as id_comentario")
    comentarios = [record['id_comentario'] for record in comentarios]   
    comentarios_random = random.sample(comentarios, min(2, len(comentarios)))
    return comentarios_random


def fecha_random():
    fecha = random.randint(1, 31)
    mes = random.randint(1, 12)
    año = random.randint(2008, 2025)
    fecha = f"{año}-{mes}-{fecha}"
    return fecha

def estado_random():
    estados = ['pendiente', 'aceptada', 'rechazada']
    estado = random.choice(estados)
    return estado

def etiqueta_random():
    etiquetas = ['Emprendimiento', 'CreadorDeContenido']
    etiqueta = random.choice(etiquetas)
    return etiqueta

def mensaje_random():
    mensajes = ['Hola, ¿cómo estás?', '¿Qué tal?', '¿Qué haces?', '¿Qué cuentas?', '¿Cómo va todo?']
    mensaje = random.choice(mensajes)
    return mensaje

def confianza_random():
    nivel_de_confianza = random.randint(1, 10)
    return nivel_de_confianza

def tipo_de_relacion_random():
    tipos_de_relacion = ['amigo', 'familiar', 'compañero de trabajo', 'compañero de clase', 'conocido']
    tipo_de_relacion = random.choice(tipos_de_relacion)
    return tipo_de_relacion

def motivo_bloqueo_reporte_random():
    motivos = ['acoso', 'spam', 'contenido inapropiado', 'otro']
    motivo = random.choice(motivos)
    return motivo

def estado_bloqueo_random():
    estados = ['pendiente', 'aceptada', 'rechazada']
    estado = random.choice(estados)
    return estado


def tipo_rol():
    estados = ['Admin', 'Miembro', 'Moderador']
    estado = random.choice(estados)
    return estado

def comentarios_reporte_random():
    comentarios = ['Espero que no vuelva a pasar', 'Por favor, no vuelvas a hacerlo', 'No me gusta lo que haces', 'No me gusta tu actitud']
    comentario = random.choice(comentarios)
    return comentario

def contexto_contenido_random():
    contextos = ['publicacion', 'comentario', 'historia']
    contexto = random.choice(contextos)
    return contexto

def visibilidad_random():
    visibilidades = ['publico', 'privado', 'solo amigos']
    visibilidad = random.choice(visibilidades)
    return visibilidad

def comentario_random():
    comentarios = ['Me encanta', 'No me gusta', 'Está bien', 'Está mal', 'No me parece']
    comentario = random.choice(comentarios)
    return comentario

def contenido_random():
    contenidos = [
        'Este es un contenido interesante.',
        'No te pierdas esto.',
        'Contenido exclusivo para ti.',
        'Mira lo que encontré.',
        'Esto es increíble.',
        'No puedo creer esto.',
        'Esto es muy útil.',
        'Espero que te guste esto.'
    ]
    contenido = random.choice(contenidos)
    return contenido

def estado_mensaje_random():
    estados = ['Enviado', 'pendiente', 'leido']
    estado = random.choice(estados)
    return estado

def tipo_random():
    estados = ['Imagen', 'Texto', 'Video']
    estado = random.choice(estados)
    return estado


def tipo_reaccion_random():
    pass