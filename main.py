from neo4j import GraphDatabase, Neo4jDriver
from dotenv import load_dotenv
import os
import pandas as pd
from insert import * 
import random
from relaciones import *
from acciones import *

load_dotenv()  # Cargar variables del archivo .env


# URI = os.getenv("NEO4J_URI")
USER = "neo4j"
# CONTRA = os.getenv("NEO4J_PASSWORD")
#--
URI ="neo4j+s://e5e3ecfb.databases.neo4j.io"
CONTRA = "c-GmqdjUkPD1QKFXIPL2gs9NEaOurpM82owa9LQ5f0E"
# driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
# session = driver.session()
users = None
usuario = None

def main():

    while True:
        global usuario
        print('\n')
        print('*'*100)
        print('* Bienvenido a Facebook Lite') 
        print('*'*100)

        print('\nEscoga una opcion \n1. Cargar Data \n2. Etiquetar usuarios \n3. Crear Relaciones\n4. Iniciar sesion\n5. Crear Usuario \n6. Crear Post \n7. ver seguidores\n8. ver eventos \n9. actualizar Info \n10. dejar de seguir \n11. eliminar cuenta \n12. ver seguidos \n13. cerrar sesion  \n14. salir')
        opcion = int(input("Ingrese una opción: "))
        if opcion == 1:
            try:
                cargarDatos()
                print("Datos cargados")
            except Exception as e:
                print("Error al cargar los datos: ", e)

        elif opcion == 2:
            try:
                etiquetas_random()
                print("etiquetas creadas")
            except Exception as e:
                print("Error al crear las etiquetas: ", e)

        elif opcion == 3:
            try: 
                crearRelaicones()
            except Exception as e:
                print("Error al crear las relaciones: ", e)

        elif opcion == 4:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            user = iniciarSesion(session)
            usuario = user
            driver.close()

        elif opcion == 5:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            user = crearUsuario(session)
            usuario = user

        elif opcion == 6:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            crearPost(session)

        elif opcion == 7:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            verSeguidores(session, usuario)
            driver.close()

        elif opcion == 8:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            verEventos(session)
            driver.close()

        elif opcion == 9:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            actualizarInfo(session)
            driver.close()

        elif opcion == 10:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            dejardeSeguir(session, usuario)
            driver.close()

        elif opcion == 11:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            eliminarCuenta(session)
            driver.close()

        elif opcion == 12:
            driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
            session = driver.session()
            verSeguidos(session, usuario)
            driver.close()

        elif opcion == 13:
            usuario = None

        elif opcion == 14:
            break;
 


# funcion para cargar los datos del csv
def cargarCSV(function, csv_file):
    df = pd.read_csv(csv_file)
    global users

    if csv_file == "./data/users.csv":
        users = df['username']

    #esto es porque cuando se creo la data, se nos fue una de default que es la de email y esa esta extra
    elif csv_file == "./data/historias.csv":
        df = df.drop('email', axis=1)

    #esto es porque al generar la data en mookaroo se generaron users que no se repetian
    elif csv_file == "./data/mensaje.csv" or csv_file == './data/comentario.csv':
        if users is not None:  
            # print('-'*100)
            df["username"] = users
            # print(df.head())
        else:
            print("error users no se ha cargado desde users.csv")
            return 
   
    driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
    print("Successfully connected to Neo4j")
    print('Cargando datos...')
    
    #Insertar datos
    with driver.session() as session:
        for _, row in df.iterrows():
            session.execute_write(function, row)

    driver.close()
    print("Importación completada.")


def etiquetas_random():
    driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))
    #asignar etiquetas a uno o mas usuarios
    with driver.session() as session:
        #etiquetas a usuarios
        result_users = session.run("MATCH (u:Usuario) RETURN u.username as username")
        usernames = [record["username"] for record in result_users]

        usuarios_random = random.sample(usernames, min(667, len(usernames)))

        for username in usuarios_random:
            etiqueta= random.choice(['Emprendimiento', 'CreadorDeContenido'])
            session.run("MATCH (u:Usuario) WHERE u.username = $username SET u:" + etiqueta, username=username)

        #etiquetas a publicaciones
        result_publicaciones = session.run("MATCH (p:Publicacion) RETURN p.id_publicacion as id_publicacion")
        publicaciones = [record["id_publicacion"] for record in result_publicaciones]
        publicaciones_random = random.sample(publicaciones, min(500, len(publicaciones)))


        for publicacion in publicaciones_random:
            etiqueta= random.choice(['foto', 'video' , 'GIF', 'Texto'])
            session.run("MATCH (p:Publicacion) WHERE p.id_publicacion = $publicacion SET p:" + etiqueta, publicacion=publicacion)

    driver.close()
    print("Etiquetas añadidas correctamente.")
    

def crearRelaicones():
    #asignar etiquetas a uno o mas usuarios
    driver = GraphDatabase.driver(URI, auth=(USER, CONTRA))

    with driver.session() as session:
        usuario_sigue_usuario(session)
        usuario_solicita_amistad_usuario(session)
        usuario_es_amigo_de_usuario(session)
        usuario_bloquea_usuario(session)
        usuario_reporta_usuario(session)
        usuario_menciona_usuario(session)
        usuario_reporta_publicacion(session)
        usuario_reporta_comentario(session)

    driver.close()
    print("relaciones añadidas correctamente.")

def CargarUsers():
    cargarCSV(insert_usuario, "./data/users.csv")
    print('usuarios correctamente cargados')

def cargarDatos():
    CargarUsers()
    cargarCSV(insert_publicacion, "./data/publicacion.csv")
    cargarCSV(insert_mensaje, "./data/mensaje.csv")
    cargarCSV(insert_comentario, "./data/comentario.csv")
    cargarCSV(insert_evento, "./data/evento.csv")
    cargarCSV(insert_grupo, "./data/grupos.csv")
    cargarCSV(insert_historia, "./data/historias.csv")

main()