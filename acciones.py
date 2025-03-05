from datetime import datetime
from relaciones import *

# CRUD

def iniciarSesion(DriverSession):
    
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    # Verificar si el usuario y contraseña son válidos

    #aledwithg
    #iX2`Q{aa!|iDu

    #sgeorgeon23
    #bO5&VVtZO)

    with DriverSession as session:
        query = "MATCH (u:Usuario {nombre: $nombre, password: $password}) RETURN u.nombre as nombre"
        resultado = session.run(query, nombre=usuario, password=password)
        
        if resultado:
            print("Bienvenido, " + usuario)
            return usuario
        else:
            print("Usuario o contraseña incorrectos")
            return None
        
    return None

#----- CREATE 
def crearUsuario(DriverSession, b):
    usuario = input("Ingrese su nombre de usuario: ")
    
    #verificar que el username no exista
    with DriverSession as session:
        query = "MATCH (u:Usuario {username: $usuario}) RETURN u"
        resultado = session.run(query, usuario=usuario)
        
        if resultado.peek() is None:
            try:
                nombre = input("Ingrese su nombre: ")
                correo = input("Ingrese su correo: ")
                detalles = input("Ingrese detalles sobre usted: ")
                foto = input("Ingrese la ruta de su foto de perfil: ")
                genero = input("Ingrese su género: ")
                fecha_nacimiento_str = input("Ingrese su fecha de nacimiento:  (en el formato de dd/mm/yyyy): ")
                fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()
                edad = datetime.now().year - fecha_nacimiento.year
                password = input("Ingrese su contraseña: ")
                
                query1 = """
                        CREATE (u:Usuario {username: $username}) 
                        SET u.correo = $correo, 
                        u.nombre = $nombre, 
                        u.detalles = $detalles, 
                        u.foto_perfil = $foto_perfil, 
                        u.edad = $edad,
                        u.genero = $genero,
                        u.fecha_nacimiento = ($fecha_nacimiento),
                        u.password = $password;
                        """
                query2 = """
                        CREATE (u:Usuario:Emprendimiento {username: $username}) 
                        SET u.correo = $correo, 
                        u.nombre = $nombre, 
                        u.detalles = $detalles, 
                        u.foto_perfil = $foto_perfil, 
                        u.edad = $edad,
                        u.genero = $genero,
                        u.fecha_nacimiento = ($fecha_nacimiento),
                        u.password = $password;
                        """
                if (b == "Y"):
                    session.run(query2, username=usuario, correo=correo, nombre=nombre, detalles=detalles, foto_perfil=foto, edad=edad, genero=genero, fecha_nacimiento=fecha_nacimiento, password=password)
                else:
                    session.run(query1, username=usuario, correo=correo, nombre=nombre, detalles=detalles, foto_perfil=foto, edad=edad, genero=genero, fecha_nacimiento=fecha_nacimiento, password=password)

                print("Bienvenido a facebook " + nombre + " !\n")

                return usuario
            
            except ValueError:
                print("fecha de nacimiento en formato incorrecto")
                return None
        
            except Exception as e:
                print("Error al crear el usuario: ", e)
                return None

        else:
            print("El username ya está en uso, pruebe con otro username")
            return None
        
    return None



        
def crearEvento(DriverSession):
    with DriverSession as session:
        try:
            # Contar el número de eventos existentes
            count_query = "MATCH (e:Evento) RETURN count(e) as count"
            count_result = session.run(count_query)
            count_record = count_result.single()
            event_count = count_record['count']
            new_event_id = event_count + 1

            # Crear el nuevo evento con el ID calculado
            query1 = """
                    CREATE (e:Evento {id_evento: $id_evento}) 
                    RETURN e
                    """
            resultado = session.run(query1, id_evento=new_event_id)
            record = resultado.single()
            id_evento = record['e']['id_evento']
            print(f"Evento creado con ID: {id_evento}")
            
            r = input("Desea especificar detalles? (Y/N): ")
            if r.upper() == "Y":
                detallesEvento(DriverSession, id_evento)
                
            print("Evento creado")
            
        except ValueError:
            print("Fecha de nacimiento en formato incorrecto")
            return None
        
        except Exception as e:
            print("Error al crear el evento: ", e)
            return None
        
    return None


#----- READ 

def verMiInfo(DriverSession, usuario):
     with DriverSession as session:
        if usuario:
            query = "MATCH (u:Usuario {username: $usuario}) RETURN u"
            resultado = session.run(query, usuario=usuario)
            for record in resultado:
                usuario_info = record['u']
                print("Nombre: ", usuario_info.get('nombre', 'N/A'))
                print("Genero: ", usuario_info.get('genero', 'N/A'))
                print("Detalles: ", usuario_info.get('detalles', 'N/A'))
                print("Cumpleaños: ", usuario_info.get('fecha_nacimiento', 'N/A'))
                print("Correo: ", usuario_info.get('correo', 'N/A'))
                print("Foto de perfil: ", usuario_info.get('foto_perfil', 'N/A'))
                print("Edad: ", usuario_info.get('edad', 'N/A'))

        else: 
            print("No se ha iniciado sesión para ver los seguidores")


def verSeguidores(DriverSession, usuario):

    with DriverSession as session:
        if usuario:
            query = "MATCH (s:Usuario)-[:SIGUE]->(u:Usuario) WHERE u.username = $usuario RETURN s.username as username"
            resultado = session.run(query, usuario=usuario)
            
            print("\nSeguidores:")
            for row in resultado:
                print(row['username'])


            print("desea ver los seguidores de otro usuario?")
            respuesta = input("si o no: ")
            if respuesta.lower() == "si":
                usuario = input("Ingrese el nombre de usuario: ")
                verSeguidores(DriverSession, usuario)
            else:
                print("Adiós!")
        else: 
            print("No se ha iniciado sesión para ver los seguidores")
            
def verSeguidos(DriverSession, usuario):
    with DriverSession as session:
        if usuario:
            query = "MATCH (u:Usuario)-[:SIGUE]->(s:Usuario) WHERE u.username = $usuario RETURN s.username as username"
            resultado = session.run(query, usuario=usuario)
            
            print("\nSeguidos:")
            for row in resultado:
                print(row['username'])



#----- ACTUALIZAR
def detallesEvento(DriverSession, id_evento):
    with DriverSession as session:
        try:
            nombre = input("Ingrese el nombre del evento: ")
            modalidad = input("Ingrese la modalidad: ")
            detalles = input("Ingrese detalles: ")
            visibilidad = input("Ingrese visibilidad: ")
            fecha_evento_str = input("Ingrese fecha del evento: (en el formato de dd/mm/yyyy): ")
            fecha_evento = datetime.strptime(fecha_evento_str, "%d/%m/%Y").date()
            
            query = """
                    MATCH (e:Evento {id_evento: $id_evento})
                    SET e.nombre = $nombre,
                        e.modalidad = $modalidad,
                        e.detalles = $detalles,
                        e.visibilidad = $visibilidad,
                        e.fecha_evento = $fecha_evento
                    RETURN e
                    """
            
            session.run(query, id_evento=id_evento, nombre=nombre, modalidad=modalidad, detalles=detalles, visibilidad=visibilidad, fecha_evento=fecha_evento)
            print(f"Detalles del evento con ID {id_evento} actualizados.")
            
        except ValueError:
            print("Fecha del evento en formato incorrecto")
            return None
        
        except Exception as e:
            print("Error al actualizar los detalles del evento: ", e)
            return None
        
    return None

# agregar etiqueta a varios eventos
def agregarEtiqueta(DriverSession, usuario):
    with DriverSession as session:
        if usuario:
            try:
                query = """
                        MATCH (u:Usuario {username: $usuario})-[:PERTENECE_A]->(e:Evento)
                        SET e.etiqueta = 'importante'
                        RETURN e
                        """
                resultado = session.run(query, usuario=usuario)
                
                # Imprimir los eventos actualizados
                print(f"Eventos relacionados con {usuario} actualizados con la etiqueta 'importante':")
                for record in resultado:
                    evento = record['e']
                    print(f"ID Evento: {evento['id_evento']}, Etiqueta: {evento['etiqueta']}")
                
                print("Todos los eventos han sido actualizados con la etiqueta 'importante'.")
            
            except Exception as e:
                print("Error al actualizar los eventos: ", e)
        else:
            print("No se ha iniciado sesión para actualizar los eventos.")

def PublicacionesPrivadas(DriverSession, usuario):
    with DriverSession as session:
        if usuario:
            try:
                query = """
                        MATCH (u:Usuario {username: $usuario})-[:PUBLICA]->(p:Publicacion)
                        SET p.visibilidad = 'privada'
                        RETURN p
                        """
                resultado = session.run(query, usuario=usuario)
                
                # Imprimir las publicaciones actualizadas
                print(f"Publicaciones de {usuario} actualizadas a 'privada':")
                for record in resultado:
                    publicacion = record['p']
                    print(f"ID Publicación: {publicacion['id_publicacion']}, Visibilidad: {publicacion['visibilidad']}")
                
                print("Todas las publicaciones han sido actualizadas a 'privada'.")
            
            except Exception as e:
                print("Error al actualizar las publicaciones: ", e)
        else:
            print("No se ha iniciado sesión para actualizar las publicaciones.") 

def actualizarDetalles(DriverSession, usuario):
    with DriverSession as session:
        if usuario:
            try:
                nombre = input("Ingrese su nuevo nombre: ")
                correo = input("Ingrese su nuevo correo: ")
                detalles = input("Ingrese nuevos detalles sobre usted: ")
                foto = input("Ingrese la nueva ruta de su foto de perfil: ")
                genero = input("Ingrese su nuevo género: ")
                fecha_nacimiento_str = input("Ingrese su nueva fecha de nacimiento: (en el formato de dd/mm/yyyy): ")
                fecha_nacimiento = datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()
                edad = datetime.now().year - fecha_nacimiento.year
                password = input("Ingrese su nueva contraseña: ")

                query = """
                        MATCH (u:Usuario {username: $usuario})
                        SET u.nombre = $nombre,
                            u.correo = $correo,
                            u.detalles = $detalles,
                            u.foto_perfil = $foto,
                            u.genero = $genero,
                            u.fecha_nacimiento = $fecha_nacimiento,
                            u.edad = $edad,
                            u.password = $password
                        RETURN u
                        """
                
                session.run(query, usuario=usuario, nombre=nombre, correo=correo, detalles=detalles, foto=foto, genero=genero, fecha_nacimiento=fecha_nacimiento, edad=edad, password=password)
                print(f"Detalles del usuario {usuario} actualizados.")
            
            except ValueError:
                print("Fecha de nacimiento en formato incorrecto")
                return None
            
            except Exception as e:
                print("Error al actualizar los detalles del usuario: ", e)
                return None
        
        else:
            print("No se ha iniciado sesión para actualizar los detalles del usuario")

# borrar la descpricpion de un post 
def borrarDescripcion(DriverSession, usuario):
    with DriverSession as session:
        if usuario:
            try:
                post_id = int(input("Ingrese el ID del post del cual desea borrar la descripción: "))
                
                query = """
                        MATCH (u:Usuario {username: $usuario})-[:PUBLICA]->(p:Publicacion {id_publicacion: $post_id})
                        REMOVE p.descripcion
                        RETURN p
                        """
                resultado = session.run(query, usuario=usuario, post_id=post_id)
                
                # Verificar si la descripción fue eliminada
                if resultado.single():
                    print(f"Descripción del post con ID {post_id} eliminada.")
                else:
                    print(f"No se encontró el post con ID {post_id} o no tiene descripción.")
            
            except Exception as e:
                print("Error al borrar la descripción del post: ", e)
        else:
            print("No se ha iniciado sesión para borrar la descripción del post.")

# eliminar la musica de todos mis posts
def eliminarMusica(DriverSession):
    pass


def seguirAlguien(DriverSession, usuario):
    with DriverSession as session:
        if usuario:
            seguir_usuario = input("Ingrese el nombre del usuario a seguir: ")

            try:
                query = """
                MATCH (seguidor:Usuario {username: $usuario}), (seguido:Usuario {username: $seguir_usuario})
                MERGE (seguidor)-[:SIGUE]->(seguido)
                """
                session.run(query, usuario=usuario, seguir_usuario=seguir_usuario)
                print(f"Has seguido a {seguir_usuario}")
            except Exception as e:
                print(f"Error al seguir a {seguir_usuario}: {e}")
                
        else:
            print("No se ha iniciado sesión para seguir a un usuario")

#------ ELIMINAR
def dejardeSeguir(DriverSession, usuario):
    with DriverSession as session:
        if usuario:

            dejar_seguir = input("Ingrese el nombre del usuario a dejar de seguir:")
            query = "MATCH (u:Usuario)-[r:SIGUE]->(s:Usuario) WHERE u.username = $usuario AND s.username = $dejar_seguir DELETE r"
            session.run(query, usuario=usuario, dejar_seguir=dejar_seguir)
            print("Has dejado de seguir a " + dejar_seguir)
            
        else:
            print("No se ha iniciado sesión para dejar de seguir a un usuario")

def eliminarCuenta(DriverSession, usuario):
    with DriverSession as session:
        if usuario:
            try:
                query = """
                        MATCH (u:Usuario {username: $usuario})
                        DETACH DELETE u
                        """
                session.run(query, usuario=usuario)
                print(f"Cuenta del usuario {usuario} eliminada junto con todas sus relaciones.")
            
            except Exception as e:
                print("Error al eliminar la cuenta del usuario: ", e)
        else:
            print("No se ha iniciado sesión para eliminar la cuenta del usuario.")

def eliminarPublicacion(session, id_publicacion):
    try:
        query = """
                MATCH (p:Publicacion {id_publicacion: $id_publicacion})
                DETACH DELETE p
                """
        session.run(query, id_publicacion=id_publicacion)
        print(f"Publicación con ID {id_publicacion} eliminada junto con todas sus relaciones.")
    except Exception as e:
        print("Error al eliminar la publicación: ", e)