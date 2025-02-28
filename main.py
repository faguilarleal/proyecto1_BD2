from neo4j import GraphDatabase, Neo4jDriver
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()  # Cargar variables del archivo .env

URI = os.getenv("NEO4J_URI")
USER = "neo4j"
CONTRA = os.getenv("NEO4J_PASSWORD")
# CONTRA1 = os.getenv("c-GmqdjUkPD1QKFXIPL2gs9NEaOurpM82owa9LQ5f0E")



def main():
    opcion = 1
    while opcion >= 1 and  opcion <=6:
        print('*'*100)
        print('\n \n1.Cargar Data \n2. \n3. \n4. \n5. \n6. \n \n \n')
        if opcion == 1:
            try:
                cargarDatos()
                print("Datos cargados")
            except Exception as e:
                print("Error al cargar los datos: ", e)

        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            pass
        elif opcion == 6:
            pass
 


# funcion para cargar los datos del csv
def cargarCSV(function, csv_file):
    df = pd.read_csv(csv_file)
    
    driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
    print("Successfully connected to Neo4j")
    
    # Insertar datos
    with driver.session() as session:
        for _, row in df.iterrows():
            session.execute_write(function, row)

    driver.close()
    print("Importación completada.")

# funcion para crear los nodos con querys 
def insert_usuario(tx, row):
    # crear usuarios 
    query = """
    MERGE (u:Usuario {username: $username}) 
    SET u.correo = $correo, 
    u.nombre = $nombre, 
    u.detalles = $detalles, 
    u.foto_perfil = $foto_perfil, 
    u.edad = $edad,u.genero = $genero,
    u.fecha_nacimiento = ($fecha_nacimiento);"""
    tx.run(query, username=row['username'], correo=row['correo'], nombre=row['nombre'], detalles=row['detalles'], foto_perfil=row['foto'], edad=row['edad'], genero=row['genero'], fecha_nacimiento=row['fecha_nacimiento'])

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

def cargarDatos():
    cargarCSV(insert_publicacion, "./data/publicacion.csv")
    cargarCSV(insert_mensaje, "./data/mensaje.csv")
    cargarCSV(insert_comentario, "./data/comentario.csv")
    cargarCSV(insert_evento, "./data/evento.csv")
    cargarCSV(insert_grupo, "./data/grupos.csv")
    cargarCSV(insert_historia, "./data/historias.csv")
