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
def crearUsuario(DriverSession):
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
                
                session.run(query, username=usuario, correo=correo, nombre=nombre, detalles=detalles, foto_perfil=foto, edad=edad, genero=genero, fecha_nacimiento=fecha_nacimiento, password=password)
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


def crearPost(DriverSession, usuario):
    pass
        


#----- READ 
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

def verEventos(DriverSession, usuario):
    pass

#----- ACTUALIZAR
def actualizarInfo(DriverSession, usuario):
    pass

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
    pass