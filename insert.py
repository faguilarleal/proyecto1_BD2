# funcion para crear los nodos con querys 
def insert_usuario(tx, row):
    # crear usuarios 
    query = """
    MERGE (u:Usuario {username: $username}) 
    SET u.correo = $correo, 
    u.nombre = $nombre, 
    u.detalles = $detalles, 
    u.foto_perfil = $foto_perfil, 
    u.edad = $edad,
    u.genero = $genero,
    u.fecha_nacimiento = ($fecha_nacimiento),
    u.password = $password;
    """
    tx.run(query, username=row['username'], correo=row['correo'], nombre=row['nombre'], detalles=row['detalles'], foto_perfil=row['foto'], edad=row['edad'], genero=row['genero'], fecha_nacimiento=row['fecha_nacimiento'], password=row['password'])

def insert_publicacion(tx, row):
    query = """
    MERGE (p:Publicacion {id_publicacion: $id_publicacion})
    SET p.likes = $likes, 
        p.etiquetas = $etiquetas, 
        p.sentimiento_actividad = $sentimiento, 
        p.descripcion = $descripcion, 
        p.musica = $musica, 
        p.foto_video = $foto, 
        p.visibilidad = $visibilidad;
    """
    tx.run(query, **row)

def insert_comentario(tx, row):
    query = """
    MERGE (c:Comentario {id_comentario: $id_comentario})
    SET c.fecha = ($fecha), 
        c.username = $username, 
        c.texto = $texto, 
        c.media = $foto;
    """
    tx.run(query, **row)


def insert_historia(tx, row):
    query = """
    MERGE (h:Historia {id_historia: $id_historia})
    SET h.imagen_video = $Imagen, 
        h.texto = $texto, 
        h.username = $username, 
        h.musica = $musica;
    """
    tx.run(query, **row)

def insert_grupo(tx, row):
    query = """
    MERGE (g:Grupo {id_grupo: $id_grupo})
    SET g.nombre = $nombre, 
        g.descripcion = $descripcion, 
        g.visibilidad = $visibilidad, 
        g.archivos = $archivos, 
        g.eventos = $eventos;
    """
    tx.run(query, **row)

def insert_mensaje(tx, row):
    query = """
    MERGE (m:Mensaje {id_mensaje: $id_mensaje})
    SET m.contenido = $contenido, 
        m.fecha = ($fecha), 
        m.hora = $hora, 
        m.receptor = $receptor;
    """
    tx.run(query, **row)

def insert_evento(tx, row):
    query = """
    MERGE (e:Evento {id_evento: $id_evento})
    SET e.nombre = $nombre, 
        e.fecha_hora = ($fecha), 
        e.modalidad = $modalidad, 
        e.visibilidad = $visibilidad, 
        e.detalle = $detalle;
    """
    tx.run(query, **row)