# CRUD
def iniciarSesion(DriverSession):
    
    usuario = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    # Verificar si el usuario y contraseña son válidos

    #aledwithg
    #iX2`Q{aa!|iDu
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
    pass

def crearPost(DriverSession, usuario):
    pass

#----- READ 
def verSeguidores(DriverSession, usuario):
    pass

def verEventos(DriverSession, usuario):
    pass

#----- ACTUALIZAR
def actualizarInfo(DriverSession, usuario):
    pass

#------ ELIMINAR
def dejardeSeguir(DriverSession, usuario):
    pass

def eliminarCuenta(DriverSession, usuario):
    pass