from neo4j import GraphDatabase, Neo4jDriver
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()  # Cargar variables del archivo .env

URI = os.getenv("NEO4J_URI")
USER = "neo4j"
CONTRA = os.getenv("NEO4J_PASSWORD")


def main():
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
def insert_publicacion(tx, row):
    # crear usuarios 
    # query = "MERGE (u:Usuario {username: $username}) SET u.correo = $correo, u.nombre = $nombre, u.detalles = $detalles, u.foto_perfil = $foto_perfil, u.edad = $edad,u.genero = $genero,u.fecha_nacimiento = ($fecha_nacimiento);"
    # tx.run(query, username=row['username'], correo=row['correo'], nombre=row['nombre'], detalles=row['detalles'], foto_perfil=row['foto'], edad=row['edad'], genero=row['genero'], fecha_nacimiento=row['fecha_nacimiento'])
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
        g.archivos = $archivos;
    """
    tx.run(query, **row)

def insert_mensaje(tx, row):
    query = """
    MERGE (m:Mensaje {id_mensaje: $id_mensaje})
    SET m.contenido = $contenido, 
        m.fecha = ($fecha), 
        m.archivos = $archivos, 
        m.receptor = $receptor;
    """
    tx.run(query, **row)

def insert_evento(tx, row):
    query = """
    MERGE (e:Evento {id_evento: $id_evento})
    SET e.nombre = $nombre, 
        e.fecha_hora = ($fecha_hora), 
        e.modalidad = $modalidad, 
        e.visibilidad = $visibilidad, 
        e.detalle = $detalle;
    """
    tx.run(query, **row)

cargarCSV(insert_publicacion, "C://Users//Francis//OneDrive - UVG//Francis//2025//Base de datos 2//proyecto1_BD2//data//publicacion.csv")
cargarCSV(insert_mensaje, "C://Users//Francis//OneDrive - UVG//Francis//2025//Base de datos 2//proyecto1_BD2//data//mensaje.csv")
cargarCSV(insert_comentario, "C://Users//Francis//OneDrive - UVG//Francis//2025//Base de datos 2//proyecto1_BD2//data//comentario.csv")
cargarCSV(insert_evento, "C://Users//Francis//OneDrive - UVG//Francis//2025//Base de datos 2//proyecto1_BD2//data//evento.csv")
cargarCSV(insert_grupo, "C://Users//Francis//OneDrive - UVG//Francis//2025//Base de datos 2//proyecto1_BD2//data//grupos.csv")
cargarCSV(insert_historia, "C://Users//Francis//OneDrive - UVG//Francis//2025//Base de datos 2//proyecto1_BD2//data//historias.csv")
