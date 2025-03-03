# CRUD

def iniciarSesion(session):
    usuario = input("Ingrese su nombre de usuario: ")
    contrasenia = input("Ingrese su contraseña: ")
    # Verificar si el usuario y contraseña son válidos
    usuarios =session.run("MATCH (u:Usuario) RETURN u.username as username")

    if usuario in usuarios:
        print("Inicio de sesión exitoso")
    else:
        print("Usuario o contraseña incorrectos")


#----- CREATE 
def crearUsuario(session):
    pass

def crearPost(session, usuario):
    pass

#----- READ 
def verSeguidores(session, usuario):
    pass

def verEventos(session, usuario):
    pass

#----- ACTUALIZAR
def actualizarInfo(session, usuario):
    pass

#------ ELIMINAR
def dejardeSeguir(session, usuario):
    pass

def eliminarCuenta(session, usuario):
    pass